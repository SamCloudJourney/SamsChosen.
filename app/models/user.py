"""User model — represents a sole trader / freelancer."""

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, new_id


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, default=new_id)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    full_name: Mapped[str] = mapped_column(String(255))

    # HMRC linkage
    hmrc_access_token: Mapped[str | None] = mapped_column(String(1024))
    hmrc_refresh_token: Mapped[str | None] = mapped_column(String(1024))
    hmrc_business_id: Mapped[str | None] = mapped_column(String(64))
    utr: Mapped[str | None] = mapped_column(String(10))  # Unique Taxpayer Reference
    nino: Mapped[str | None] = mapped_column(String(9))  # National Insurance Number

    # Open Banking linkage
    bank_access_token: Mapped[str | None] = mapped_column(String(1024))
    bank_refresh_token: Mapped[str | None] = mapped_column(String(1024))
    bank_consent_id: Mapped[str | None] = mapped_column(String(255))

    # Settings
    uses_simplified_expenses: Mapped[bool] = mapped_column(Boolean, default=True)
    vat_registered: Mapped[bool] = mapped_column(Boolean, default=False)
    home_office_hours_per_month: Mapped[int | None] = mapped_column()

    transactions: Mapped[list["BankTransaction"]] = relationship(back_populates="user")  # noqa: F821

    def __repr__(self) -> str:
        return f"<User {self.email}>"
