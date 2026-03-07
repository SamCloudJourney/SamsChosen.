"""Pydantic schemas for API request/response models."""

from datetime import date
from decimal import Decimal

from pydantic import BaseModel, EmailStr

from app.models.transaction import SA103Category, TransactionType


# ── Auth ───────────────────────────────────────────────────────────────

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str


class UserResponse(BaseModel):
    id: str
    email: str
    full_name: str
    hmrc_connected: bool
    bank_connected: bool
    vat_registered: bool

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ── Transactions ───────────────────────────────────────────────────────

class TransactionResponse(BaseModel):
    id: str
    transaction_date: date
    description: str
    amount: Decimal
    currency: str
    transaction_type: TransactionType
    category: SA103Category
    category_confidence: float | None
    manually_categorised: bool
    tax_quarter: int | None
    tax_year: str | None
    notes: str | None

    model_config = {"from_attributes": True}


class TransactionCategorise(BaseModel):
    category: SA103Category


class TransactionSummary(BaseModel):
    total_income: Decimal
    total_expenses: Decimal
    net_profit: Decimal
    expenses_by_category: dict[str, Decimal]
    transaction_count: int
    uncategorised_count: int


# ── Tax ────────────────────────────────────────────────────────────────

class TaxEstimateResponse(BaseModel):
    gross_income: Decimal
    total_expenses: Decimal
    net_profit: Decimal
    personal_allowance: Decimal
    taxable_income: Decimal
    basic_rate_tax: Decimal
    higher_rate_tax: Decimal
    additional_rate_tax: Decimal
    total_income_tax: Decimal
    class_2_nic: Decimal
    class_4_nic: Decimal
    total_nic: Decimal
    total_tax_due: Decimal
    effective_rate: Decimal
    approaching_vat_threshold: bool
    suggested_monthly_set_aside: Decimal


# ── Banking ────────────────────────────────────────────────────────────

class BankAuthResponse(BaseModel):
    auth_url: str


class BankAccount(BaseModel):
    account_id: str
    display_name: str | None
    provider: str | None
    currency: str | None


# ── HMRC ───────────────────────────────────────────────────────────────

class HMRCAuthResponse(BaseModel):
    auth_url: str


class ObligationResponse(BaseModel):
    tax_year: str
    period_start: date
    period_end: date
    due_date: date
    status: str


class QuarterlySubmitRequest(BaseModel):
    tax_year: str
    period_start: date
    period_end: date
    consolidated: bool = True
