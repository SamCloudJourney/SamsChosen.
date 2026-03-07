"""Transaction model — bank transactions linked to tax categories."""

from datetime import date
from decimal import Decimal
from enum import Enum

from sqlalchemy import Date, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, new_id


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class SA103Category(str, Enum):
    """SA103F expense categories mapped to HMRC box numbers."""

    TURNOVER = "turnover"  # Box 15/16 — income
    COST_OF_GOODS = "cost_of_goods"  # Box 17
    CIS_PAYMENTS = "cis_payments"  # Box 18
    STAFF_COSTS = "staff_costs"  # Box 19
    TRAVEL = "travel"  # Box 20
    PREMISES = "premises"  # Box 21
    REPAIRS = "repairs"  # Box 22
    OFFICE_COSTS = "office_costs"  # Box 23
    ADVERTISING = "advertising"  # Box 24
    LOAN_INTEREST = "loan_interest"  # Box 25
    FINANCIAL_CHARGES = "financial_charges"  # Box 26
    BAD_DEBTS = "bad_debts"  # Box 27
    DEPRECIATION = "depreciation"  # Box 28 — not allowable
    OTHER_EXPENSES = "other_expenses"  # Box 29
    USE_OF_HOME = "use_of_home"  # Box 30
    UNCATEGORISED = "uncategorised"


# Map SA103 categories to their HMRC box numbers
SA103_BOX_MAP: dict[SA103Category, int | None] = {
    SA103Category.TURNOVER: 15,
    SA103Category.COST_OF_GOODS: 17,
    SA103Category.CIS_PAYMENTS: 18,
    SA103Category.STAFF_COSTS: 19,
    SA103Category.TRAVEL: 20,
    SA103Category.PREMISES: 21,
    SA103Category.REPAIRS: 22,
    SA103Category.OFFICE_COSTS: 23,
    SA103Category.ADVERTISING: 24,
    SA103Category.LOAN_INTEREST: 25,
    SA103Category.FINANCIAL_CHARGES: 26,
    SA103Category.BAD_DEBTS: 27,
    SA103Category.DEPRECIATION: 28,
    SA103Category.OTHER_EXPENSES: 29,
    SA103Category.USE_OF_HOME: 30,
    SA103Category.UNCATEGORISED: None,
}


class BankTransaction(Base, TimestampMixin):
    __tablename__ = "transactions"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, default=new_id)
    user_id: Mapped[str] = mapped_column(String(32), ForeignKey("users.id"), index=True)

    # Bank data
    bank_transaction_id: Mapped[str | None] = mapped_column(String(255), unique=True)
    transaction_date: Mapped[date] = mapped_column(Date, index=True)
    description: Mapped[str] = mapped_column(Text)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    currency: Mapped[str] = mapped_column(String(3), default="GBP")

    # Classification
    transaction_type: Mapped[TransactionType] = mapped_column(String(10))
    category: Mapped[SA103Category] = mapped_column(
        String(30), default=SA103Category.UNCATEGORISED
    )
    category_confidence: Mapped[float | None] = mapped_column()  # 0.0-1.0
    manually_categorised: Mapped[bool] = mapped_column(default=False)

    # Tax quarter (1-4, for the tax year Apr-Mar)
    tax_quarter: Mapped[int | None] = mapped_column()
    tax_year: Mapped[str | None] = mapped_column(String(7))  # e.g. "2026-27"

    # Optional receipt
    receipt_url: Mapped[str | None] = mapped_column(String(500))

    notes: Mapped[str | None] = mapped_column(Text)

    user: Mapped["User"] = relationship(back_populates="transactions")  # noqa: F821

    def __repr__(self) -> str:
        return f"<Transaction {self.transaction_date} {self.amount} {self.category}>"
