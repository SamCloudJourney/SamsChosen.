"""HMRC MTD obligation tracking."""

from datetime import date
from enum import Enum

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, new_id


class ObligationStatus(str, Enum):
    OPEN = "open"
    FULFILLED = "fulfilled"


class Obligation(Base, TimestampMixin):
    """Tracks HMRC quarterly obligation deadlines and submission status."""

    __tablename__ = "obligations"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, default=new_id)
    user_id: Mapped[str] = mapped_column(String(32), ForeignKey("users.id"), index=True)

    tax_year: Mapped[str] = mapped_column(String(7))  # e.g. "2026-27"
    period_start: Mapped[date] = mapped_column(Date)
    period_end: Mapped[date] = mapped_column(Date)
    due_date: Mapped[date] = mapped_column(Date)
    status: Mapped[ObligationStatus] = mapped_column(String(10), default=ObligationStatus.OPEN)
    hmrc_period_key: Mapped[str | None] = mapped_column(String(10))

    def __repr__(self) -> str:
        return f"<Obligation {self.tax_year} {self.period_start}-{self.period_end} {self.status}>"
