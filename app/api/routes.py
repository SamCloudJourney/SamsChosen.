"""FastAPI routes — the main API surface for the bookkeeping MVP."""

from datetime import date
from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.integrations.hmrc import hmrc_client
from app.integrations.truelayer import truelayer_client
from app.models.transaction import SA103Category, Transaction, TransactionType
from app.models.user import User
from app.services.categoriser import categorise_transaction
from app.services.tax_calculator import compute_tax
from app.api.schemas import (
    BankAccount,
    BankAuthResponse,
    HMRCAuthResponse,
    ObligationResponse,
    QuarterlySubmitRequest,
    TaxEstimateResponse,
    TransactionCategorise,
    TransactionResponse,
    TransactionSummary,
    UserCreate,
    UserResponse,
)

router = APIRouter()


# ── Helpers ────────────────────────────────────────────────────────────

async def _get_user(user_id: str, db: AsyncSession) -> User:
    """Fetch a user or raise 404."""
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def _tax_year_for_date(d: date) -> str:
    """Determine UK tax year string (e.g. '2026-27') for a given date."""
    if d.month >= 4 and d.day >= 6 or d.month > 4:
        return f"{d.year}-{str(d.year + 1)[2:]}"
    return f"{d.year - 1}-{str(d.year)[2:]}"


def _tax_quarter_for_date(d: date) -> int:
    """Determine which MTD quarter (1-4) a date falls into."""
    if d.month in (4, 5, 6) or (d.month == 4 and d.day >= 6):
        return 1
    if d.month in (7, 8, 9):
        return 2
    if d.month in (10, 11, 12):
        return 3
    return 4  # Jan-Apr 5


# ── User ───────────────────────────────────────────────────────────────

@router.post("/users", response_model=UserResponse)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)):
    """Register a new sole trader / freelancer."""
    from passlib.hash import bcrypt

    existing = await db.execute(select(User).where(User.email == body.email))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email already registered")

    user = User(
        email=body.email,
        hashed_password=bcrypt.hash(body.password),
        full_name=body.full_name,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return UserResponse(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        hmrc_connected=bool(user.hmrc_access_token),
        bank_connected=bool(user.bank_access_token),
        vat_registered=user.vat_registered,
    )


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, db: AsyncSession = Depends(get_db)):
    user = await _get_user(user_id, db)
    return UserResponse(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        hmrc_connected=bool(user.hmrc_access_token),
        bank_connected=bool(user.bank_access_token),
        vat_registered=user.vat_registered,
    )


# ── Banking ────────────────────────────────────────────────────────────

@router.get("/banking/connect/{user_id}", response_model=BankAuthResponse)
async def connect_bank(user_id: str, db: AsyncSession = Depends(get_db)):
    """Start Open Banking consent flow."""
    await _get_user(user_id, db)  # verify user exists
    auth_url = truelayer_client.get_auth_link(state=user_id)
    return BankAuthResponse(auth_url=auth_url)


@router.get("/banking/callback")
async def banking_callback(
    code: str, state: str, db: AsyncSession = Depends(get_db)
):
    """Handle TrueLayer OAuth callback."""
    user = await _get_user(state, db)
    tokens = await truelayer_client.exchange_code(code)

    user.bank_access_token = tokens["access_token"]
    user.bank_refresh_token = tokens.get("refresh_token")
    await db.commit()

    return {"status": "connected"}


@router.get("/banking/accounts/{user_id}", response_model=list[BankAccount])
async def list_bank_accounts(user_id: str, db: AsyncSession = Depends(get_db)):
    """List connected bank accounts."""
    user = await _get_user(user_id, db)
    if not user.bank_access_token:
        raise HTTPException(status_code=400, detail="Bank not connected")

    accounts = await truelayer_client.get_accounts(user.bank_access_token)
    return [
        BankAccount(
            account_id=a["account_id"],
            display_name=a.get("display_name"),
            provider=a.get("provider", {}).get("display_name"),
            currency=a.get("currency"),
        )
        for a in accounts
    ]


@router.post("/banking/sync/{user_id}")
async def sync_transactions(
    user_id: str,
    account_id: str = Query(...),
    db: AsyncSession = Depends(get_db),
):
    """Pull transactions from bank and auto-categorise them."""
    user = await _get_user(user_id, db)
    if not user.bank_access_token:
        raise HTTPException(status_code=400, detail="Bank not connected")

    raw_txns = await truelayer_client.get_transactions(user.bank_access_token, account_id)

    created = 0
    for txn in raw_txns:
        bank_id = txn.get("transaction_id")
        # Skip duplicates
        existing = await db.execute(
            select(Transaction).where(Transaction.bank_transaction_id == bank_id)
        )
        if existing.scalar_one_or_none():
            continue

        amount = float(txn.get("amount", 0))
        description = txn.get("description", "")

        cat_result = categorise_transaction(description, amount)
        txn_date = date.fromisoformat(txn["timestamp"][:10])

        record = Transaction(
            user_id=user_id,
            bank_transaction_id=bank_id,
            transaction_date=txn_date,
            description=description,
            amount=Decimal(str(amount)),
            transaction_type=cat_result.transaction_type.value,
            category=cat_result.category.value,
            category_confidence=cat_result.confidence,
            tax_quarter=_tax_quarter_for_date(txn_date),
            tax_year=_tax_year_for_date(txn_date),
        )
        db.add(record)
        created += 1

    await db.commit()
    return {"synced": created, "total_from_bank": len(raw_txns)}


# ── Transactions ───────────────────────────────────────────────────────

@router.get("/transactions/{user_id}", response_model=list[TransactionResponse])
async def list_transactions(
    user_id: str,
    tax_year: str | None = None,
    quarter: int | None = None,
    category: SA103Category | None = None,
    db: AsyncSession = Depends(get_db),
):
    """List transactions with optional filters."""
    query = select(Transaction).where(Transaction.user_id == user_id)
    if tax_year:
        query = query.where(Transaction.tax_year == tax_year)
    if quarter:
        query = query.where(Transaction.tax_quarter == quarter)
    if category:
        query = query.where(Transaction.category == category)
    query = query.order_by(Transaction.transaction_date.desc())

    result = await db.execute(query)
    return result.scalars().all()


@router.put("/transactions/{transaction_id}/categorise", response_model=TransactionResponse)
async def recategorise_transaction(
    transaction_id: str,
    body: TransactionCategorise,
    db: AsyncSession = Depends(get_db),
):
    """Manually override the category of a transaction."""
    txn = await db.get(Transaction, transaction_id)
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")

    txn.category = body.category
    txn.manually_categorised = True
    txn.category_confidence = 1.0
    await db.commit()
    await db.refresh(txn)
    return txn


@router.get("/transactions/{user_id}/summary", response_model=TransactionSummary)
async def transaction_summary(
    user_id: str,
    tax_year: str | None = None,
    quarter: int | None = None,
    db: AsyncSession = Depends(get_db),
):
    """Get income/expense summary with category breakdown."""
    base = select(Transaction).where(Transaction.user_id == user_id)
    if tax_year:
        base = base.where(Transaction.tax_year == tax_year)
    if quarter:
        base = base.where(Transaction.tax_quarter == quarter)

    result = await db.execute(base)
    txns = result.scalars().all()

    total_income = Decimal("0")
    total_expenses = Decimal("0")
    by_category: dict[str, Decimal] = {}
    uncategorised = 0

    for t in txns:
        if t.transaction_type == TransactionType.INCOME:
            total_income += t.amount
        else:
            total_expenses += abs(t.amount)
            cat_name = t.category if isinstance(t.category, str) else t.category.value
            by_category[cat_name] = by_category.get(cat_name, Decimal("0")) + abs(t.amount)

        if t.category == SA103Category.UNCATEGORISED:
            uncategorised += 1

    return TransactionSummary(
        total_income=total_income,
        total_expenses=total_expenses,
        net_profit=total_income - total_expenses,
        expenses_by_category=by_category,
        transaction_count=len(txns),
        uncategorised_count=uncategorised,
    )


# ── Tax ────────────────────────────────────────────────────────────────

@router.get("/tax/estimate/{user_id}", response_model=TaxEstimateResponse)
async def tax_estimate(
    user_id: str,
    tax_year: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    """Real-time tax estimate based on current transactions."""
    await _get_user(user_id, db)

    base = select(Transaction).where(Transaction.user_id == user_id)
    if tax_year:
        base = base.where(Transaction.tax_year == tax_year)

    result = await db.execute(base)
    txns = result.scalars().all()

    income = sum(t.amount for t in txns if t.transaction_type == TransactionType.INCOME)
    expenses = sum(abs(t.amount) for t in txns if t.transaction_type == TransactionType.EXPENSE)

    breakdown = compute_tax(Decimal(str(income)), Decimal(str(expenses)))

    return TaxEstimateResponse(
        gross_income=breakdown.gross_income,
        total_expenses=breakdown.total_expenses,
        net_profit=breakdown.net_profit,
        personal_allowance=breakdown.personal_allowance,
        taxable_income=breakdown.taxable_income,
        basic_rate_tax=breakdown.basic_rate_tax,
        higher_rate_tax=breakdown.higher_rate_tax,
        additional_rate_tax=breakdown.additional_rate_tax,
        total_income_tax=breakdown.total_income_tax,
        class_2_nic=breakdown.class_2_nic,
        class_4_nic=breakdown.class_4_nic,
        total_nic=breakdown.total_nic,
        total_tax_due=breakdown.total_tax_due,
        effective_rate=breakdown.effective_rate,
        approaching_vat_threshold=breakdown.approaching_vat_threshold,
        suggested_monthly_set_aside=breakdown.suggested_monthly_set_aside,
    )


# ── HMRC ───────────────────────────────────────────────────────────────

@router.get("/hmrc/connect/{user_id}", response_model=HMRCAuthResponse)
async def connect_hmrc(user_id: str, db: AsyncSession = Depends(get_db)):
    """Start HMRC OAuth flow."""
    await _get_user(user_id, db)
    auth_url = hmrc_client.get_auth_url(state=user_id)
    return HMRCAuthResponse(auth_url=auth_url)


@router.get("/hmrc/callback")
async def hmrc_callback(code: str, state: str, db: AsyncSession = Depends(get_db)):
    """Handle HMRC OAuth callback."""
    user = await _get_user(state, db)
    tokens = await hmrc_client.exchange_code(code)

    user.hmrc_access_token = tokens["access_token"]
    user.hmrc_refresh_token = tokens.get("refresh_token")
    await db.commit()

    return {"status": "connected"}


@router.get("/hmrc/obligations/{user_id}", response_model=list[ObligationResponse])
async def get_obligations(
    user_id: str,
    tax_year: str = Query(..., description="e.g. 2026-27"),
    db: AsyncSession = Depends(get_db),
):
    """Get quarterly obligation deadlines from HMRC."""
    user = await _get_user(user_id, db)
    if not user.hmrc_access_token or not user.nino:
        raise HTTPException(status_code=400, detail="HMRC not connected or NINO missing")

    obligations = await hmrc_client.get_obligations(
        user.hmrc_access_token, user.nino, tax_year
    )
    result = []
    for group in obligations:
        for ob in group.get("obligationDetails", []):
            result.append(
                ObligationResponse(
                    tax_year=tax_year,
                    period_start=ob["periodStartDate"],
                    period_end=ob["periodEndDate"],
                    due_date=ob["dueDate"],
                    status=ob["status"],
                )
            )
    return result


@router.post("/hmrc/submit/{user_id}")
async def submit_quarterly(
    user_id: str,
    body: QuarterlySubmitRequest,
    db: AsyncSession = Depends(get_db),
):
    """Submit a quarterly update to HMRC MTD."""
    user = await _get_user(user_id, db)
    if not user.hmrc_access_token or not user.nino or not user.hmrc_business_id:
        raise HTTPException(status_code=400, detail="HMRC not fully connected")

    # Gather transactions for the period
    txns_result = await db.execute(
        select(Transaction).where(
            Transaction.user_id == user_id,
            Transaction.transaction_date >= body.period_start,
            Transaction.transaction_date <= body.period_end,
        )
    )
    txns = txns_result.scalars().all()

    income = sum(t.amount for t in txns if t.transaction_type == TransactionType.INCOME)
    expenses_by_cat: dict[SA103Category, Decimal] = {}
    for t in txns:
        if t.transaction_type == TransactionType.EXPENSE:
            cat = t.category if isinstance(t.category, SA103Category) else SA103Category(t.category)
            expenses_by_cat[cat] = expenses_by_cat.get(cat, Decimal("0")) + abs(t.amount)

    result = await hmrc_client.submit_quarterly_update(
        access_token=user.hmrc_access_token,
        nino=user.nino,
        business_id=user.hmrc_business_id,
        tax_year=body.tax_year,
        period_start=body.period_start,
        period_end=body.period_end,
        income=Decimal(str(income)),
        expenses_by_category=expenses_by_cat,
        consolidated=body.consolidated,
    )

    return {"status": "submitted", "hmrc_response": result}
