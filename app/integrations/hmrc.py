"""HMRC Making Tax Digital (MTD) API integration.

Handles OAuth, obligation retrieval, and quarterly submission for Income Tax Self Assessment.
"""

from datetime import date
from decimal import Decimal
from typing import Any
from urllib.parse import urlencode

import httpx

from app.config import settings
from app.models.transaction import SA103Category

_SANDBOX_URL = "https://test-api.service.hmrc.gov.uk"
_PROD_URL = "https://api.service.hmrc.gov.uk"


def _base_url() -> str:
    return _SANDBOX_URL if settings.hmrc_sandbox else _PROD_URL


class HMRCClient:
    """Client for HMRC MTD for Income Tax APIs."""

    def __init__(self) -> None:
        self.client = httpx.AsyncClient(timeout=30.0)

    async def close(self) -> None:
        await self.client.aclose()

    # ── OAuth ──────────────────────────────────────────────────────────

    def get_auth_url(self, state: str) -> str:
        """Generate OAuth URL for user to authorise HMRC access."""
        params = {
            "response_type": "code",
            "client_id": settings.hmrc_client_id,
            "redirect_uri": settings.hmrc_redirect_uri,
            "scope": "read:self-assessment write:self-assessment",
            "state": state,
        }
        return f"{_base_url()}/oauth/authorize?{urlencode(params)}"

    async def exchange_code(self, code: str) -> dict[str, Any]:
        """Exchange auth code for access + refresh tokens."""
        resp = await self.client.post(
            f"{_base_url()}/oauth/token",
            data={
                "grant_type": "authorization_code",
                "client_id": settings.hmrc_client_id,
                "client_secret": settings.hmrc_client_secret,
                "redirect_uri": settings.hmrc_redirect_uri,
                "code": code,
            },
        )
        resp.raise_for_status()
        return resp.json()

    async def refresh_access_token(self, refresh_token: str) -> dict[str, Any]:
        """Refresh an expired access token."""
        resp = await self.client.post(
            f"{_base_url()}/oauth/token",
            data={
                "grant_type": "refresh_token",
                "client_id": settings.hmrc_client_id,
                "client_secret": settings.hmrc_client_secret,
                "refresh_token": refresh_token,
            },
        )
        resp.raise_for_status()
        return resp.json()

    def _headers(self, access_token: str) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/vnd.hmrc.3.0+json",
            "Content-Type": "application/json",
        }

    # ── Business ───────────────────────────────────────────────────────

    async def list_businesses(self, access_token: str, nino: str) -> list[dict[str, Any]]:
        """List all self-employment businesses for a taxpayer."""
        resp = await self.client.get(
            f"{_base_url()}/individuals/business/details/{nino}/list",
            headers=self._headers(access_token),
        )
        resp.raise_for_status()
        return resp.json().get("listOfBusinesses", [])

    # ── Obligations ────────────────────────────────────────────────────

    async def get_obligations(
        self,
        access_token: str,
        nino: str,
        tax_year: str,  # e.g. "2026-27"
    ) -> list[dict[str, Any]]:
        """Retrieve quarterly obligation periods and their statuses."""
        # Convert tax year format: "2026-27" -> from=2026-04-06&to=2027-04-05
        start_year = int(tax_year.split("-")[0])
        from_date = f"{start_year}-04-06"
        to_date = f"{start_year + 1}-04-05"

        resp = await self.client.get(
            f"{_base_url()}/obligations/details/{nino}/income-and-expenditure",
            headers=self._headers(access_token),
            params={"from": from_date, "to": to_date},
        )
        resp.raise_for_status()
        return resp.json().get("obligations", [])

    # ── Quarterly Submission ───────────────────────────────────────────

    async def submit_quarterly_update(
        self,
        access_token: str,
        nino: str,
        business_id: str,
        tax_year: str,
        period_start: date,
        period_end: date,
        income: Decimal,
        expenses_by_category: dict[SA103Category, Decimal],
        consolidated: bool = False,
    ) -> dict[str, Any]:
        """Submit a quarterly income/expense update to HMRC.

        If consolidated=True, submits a single total expense figure
        (allowed for turnover under GBP 90,000).
        """
        body: dict[str, Any] = {
            "periodDates": {
                "periodStartDate": period_start.isoformat(),
                "periodEndDate": period_end.isoformat(),
            },
            "periodIncome": {
                "turnover": float(income),
                "other": 0.0,
            },
        }

        if consolidated:
            total_expenses = sum(
                v for k, v in expenses_by_category.items()
                if k not in (SA103Category.UNCATEGORISED, SA103Category.DEPRECIATION)
            )
            body["periodExpenses"] = {"consolidatedExpenses": float(total_expenses)}
        else:
            body["periodExpenses"] = _build_expense_breakdown(expenses_by_category)

        resp = await self.client.put(
            f"{_base_url()}/individuals/business/self-employment/"
            f"{nino}/{business_id}/period/{tax_year}",
            headers=self._headers(access_token),
            json=body,
        )
        resp.raise_for_status()
        return resp.json() if resp.content else {"status": "ok"}

    # ── End of Period Statement ─────────────────────────────────────────

    async def submit_end_of_period(
        self,
        access_token: str,
        nino: str,
        business_id: str,
        tax_year: str,
    ) -> dict[str, Any]:
        """Submit the End of Period Statement (EOPS) for a tax year."""
        start_year = int(tax_year.split("-")[0])

        body = {
            "typeOfBusiness": "self-employment",
            "businessId": business_id,
            "accountingPeriod": {
                "startDate": f"{start_year}-04-06",
                "endDate": f"{start_year + 1}-04-05",
            },
            "finalised": True,
        }
        resp = await self.client.post(
            f"{_base_url()}/individuals/business/end-of-period-statement/{nino}",
            headers=self._headers(access_token),
            json=body,
        )
        resp.raise_for_status()
        return resp.json() if resp.content else {"status": "ok"}

    # ── Tax Calculation ────────────────────────────────────────────────

    async def trigger_calculation(
        self, access_token: str, nino: str, tax_year: str
    ) -> dict[str, Any]:
        """Trigger an in-year or final tax calculation."""
        resp = await self.client.post(
            f"{_base_url()}/individuals/calculations/{nino}/self-assessment/{tax_year}",
            headers=self._headers(access_token),
            json={},
        )
        resp.raise_for_status()
        return resp.json()

    async def get_calculation(
        self, access_token: str, nino: str, tax_year: str, calculation_id: str
    ) -> dict[str, Any]:
        """Retrieve a completed tax calculation."""
        resp = await self.client.get(
            f"{_base_url()}/individuals/calculations/{nino}/self-assessment/"
            f"{tax_year}/{calculation_id}",
            headers=self._headers(access_token),
        )
        resp.raise_for_status()
        return resp.json()


def _build_expense_breakdown(
    expenses: dict[SA103Category, Decimal],
) -> dict[str, float]:
    """Map SA103 categories to the HMRC API expense field names."""
    field_map: dict[SA103Category, str] = {
        SA103Category.COST_OF_GOODS: "costOfGoods",
        SA103Category.CIS_PAYMENTS: "cisDeductions",
        SA103Category.STAFF_COSTS: "staffCosts",
        SA103Category.TRAVEL: "travelCosts",
        SA103Category.PREMISES: "premisesRunningCosts",
        SA103Category.REPAIRS: "maintenanceCosts",
        SA103Category.OFFICE_COSTS: "adminCosts",
        SA103Category.ADVERTISING: "advertisingCosts",
        SA103Category.LOAN_INTEREST: "interestOnBankOtherLoans",
        SA103Category.FINANCIAL_CHARGES: "financeCharges",
        SA103Category.BAD_DEBTS: "irrecoverableDebts",
        SA103Category.OTHER_EXPENSES: "other",
    }
    result = {}
    for cat, field_name in field_map.items():
        if cat in expenses and expenses[cat]:
            result[field_name] = float(expenses[cat])
    return result


hmrc_client = HMRCClient()
