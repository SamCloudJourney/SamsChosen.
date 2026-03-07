"""Demo data seeder — populates realistic UK freelancer transactions."""

import hashlib
import random
from datetime import date, timedelta
from decimal import Decimal

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.transaction import BankTransaction as Transaction, TransactionType, SA103Category
from app.models.user import User
from app.models.base import new_id
from app.services.categoriser import categorise_transaction

demo_router = APIRouter()

DEMO_EMAIL = "demo@samschosen.co.uk"

# Realistic UK freelancer transactions
DEMO_TRANSACTIONS = [
    # Income
    ("BACS CREDIT ACME DIGITAL LTD", 3500.00),
    ("FASTER PAYMENT IN - INVOICE 1041", 2200.00),
    ("BACS CREDIT WIDGETS CO", 1800.00),
    ("FASTER PAYMENT IN - INVOICE 1042", 4500.00),
    ("BANK GIRO CREDIT - CONSULTING FEE", 1250.00),
    ("BACS CREDIT TECHSTARTUP LTD", 3000.00),
    ("FASTER PAYMENT IN - INVOICE 1043", 2750.00),
    ("BACS CREDIT ACME DIGITAL LTD", 3500.00),
    ("FASTER PAYMENT IN - RETAINER FEB", 2000.00),
    ("BACS CREDIT WIDGETS CO", 1800.00),
    # Travel
    ("TFL OYSTER AUTO TOPUP", -20.00),
    ("UBER TRIP LONDON EC2", -15.50),
    ("TRAINLINE LONDON-MANCHESTER", -87.00),
    ("SHELL PETROL STATION M1", -65.00),
    ("PREMIER INN MANCHESTER", -89.00),
    ("TFL OYSTER AUTO TOPUP", -20.00),
    ("BOLT RIDE SHOREDITCH", -12.40),
    # Office costs
    ("GITHUB PRO MONTHLY", -4.00),
    ("ZOOM VIDEO COMMUNICATIONS", -13.99),
    ("VODAFONE MONTHLY BILL", -28.00),
    ("MICROSOFT 365 BUSINESS", -9.40),
    ("NOTION PLUS PLAN", -8.00),
    ("SLACK TECHNOLOGIES", -6.67),
    ("ROYAL MAIL POSTAGE", -4.50),
    ("BT BROADBAND MONTHLY", -32.99),
    ("FIGMA PROFESSIONAL", -12.00),
    ("AWS SERVICES MONTHLY", -23.41),
    # Advertising
    ("GOOGLE ADS PAYMENT", -150.00),
    ("FACEBOOK ADS - META ADS", -75.00),
    ("SQUARESPACE WEBSITE ANNUAL", -144.00),
    ("NAMECHEAP DOMAIN RENEWAL", -12.99),
    # Premises
    ("WEWORK MONTHLY HOT DESK", -200.00),
    ("WEWORK MONTHLY HOT DESK", -200.00),
    # Financial
    ("MONTHLY BANK CHARGE", -5.50),
    ("STRIPE PROCESSING FEE", -32.10),
    ("STRIPE PROCESSING FEE", -24.80),
    ("PAYPAL TRANSACTION FEE", -8.90),
    # Professional / Other
    ("IPSE MEMBERSHIP ANNUAL", -119.00),
    ("PROFESSIONAL INDEMNITY INSURANCE", -45.00),
    ("XERO ACCOUNTING SOFTWARE", -0.00),  # will be replaced by us!
    ("CPD ONLINE COURSE - UDEMY", -14.99),
    ("ACCOUNTANT QUARTERLY REVIEW", -150.00),
    # Uncategorised
    ("PAYMENT TO J SMITH REF 4421", -85.00),
    ("DIRECT DEBIT - UNKNOWN REF", -29.99),
]


def _tax_year_for_date(d: date) -> str:
    if d.month > 4 or (d.month == 4 and d.day >= 6):
        return f"{d.year}-{str(d.year + 1)[2:]}"
    return f"{d.year - 1}-{str(d.year)[2:]}"


def _tax_quarter_for_date(d: date) -> int:
    if d.month in (4, 5, 6):
        return 1
    if d.month in (7, 8, 9):
        return 2
    if d.month in (10, 11, 12):
        return 3
    return 4


@demo_router.post("/seed")
async def seed_demo_data(db: AsyncSession = Depends(get_db)):
    """Create demo user with realistic transaction data."""

    # Find or create demo user
    result = await db.execute(select(User).where(User.email == DEMO_EMAIL))
    user = result.scalar_one_or_none()

    if not user:
        user = User(
            email=DEMO_EMAIL,
            hashed_password=hashlib.sha256(b"demo").hexdigest(),
            full_name="Sam Cloud",
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

    # Check if already seeded
    txn_count = await db.execute(
        select(Transaction).where(Transaction.user_id == user.id).limit(1)
    )
    if txn_count.scalar_one_or_none():
        return {"status": "already_seeded", "user_id": user.id}

    # Create transactions spread across recent months
    today = date.today()
    random.seed(42)  # deterministic for consistency

    for i, (desc, amount) in enumerate(DEMO_TRANSACTIONS):
        # Spread over last 90 days
        days_ago = random.randint(1, 90)
        txn_date = today - timedelta(days=days_ago)

        cat_result = categorise_transaction(desc, amount)

        txn = Transaction(
            id=new_id(),
            user_id=user.id,
            bank_transaction_id=f"demo-{i}-{new_id()[:8]}",
            transaction_date=txn_date,
            description=desc,
            amount=Decimal(str(amount)),
            transaction_type=cat_result.transaction_type.value,
            category=cat_result.category.value,
            category_confidence=cat_result.confidence,
            tax_quarter=_tax_quarter_for_date(txn_date),
            tax_year=_tax_year_for_date(txn_date),
        )
        db.add(txn)

    await db.commit()

    return {
        "status": "seeded",
        "user_id": user.id,
        "transactions_created": len(DEMO_TRANSACTIONS),
    }
