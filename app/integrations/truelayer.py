"""TrueLayer Open Banking integration.

Handles OAuth flow and transaction retrieval from UK bank accounts.
"""

from datetime import datetime, timedelta
from typing import Any
from urllib.parse import urlencode

import httpx

from app.config import settings

_SANDBOX_AUTH_URL = "https://auth.truelayer-sandbox.com"
_SANDBOX_API_URL = "https://api.truelayer-sandbox.com"
_PROD_AUTH_URL = "https://auth.truelayer.com"
_PROD_API_URL = "https://api.truelayer.com"


def _auth_url() -> str:
    return _SANDBOX_AUTH_URL if settings.truelayer_sandbox else _PROD_AUTH_URL


def _api_url() -> str:
    return _SANDBOX_API_URL if settings.truelayer_sandbox else _PROD_API_URL


class TrueLayerClient:
    """Client for TrueLayer Open Banking API."""

    def __init__(self) -> None:
        self.client = httpx.AsyncClient(timeout=30.0)

    async def close(self) -> None:
        await self.client.aclose()

    def get_auth_link(self, state: str) -> str:
        """Generate the OAuth consent URL for a user to connect their bank."""
        params = {
            "response_type": "code",
            "client_id": settings.truelayer_client_id,
            "redirect_uri": settings.truelayer_redirect_uri,
            "scope": "info accounts balance cards transactions",
            "providers": "uk-ob-all uk-oauth-all",
            "state": state,
        }
        return f"{_auth_url()}/?{urlencode(params)}"

    async def exchange_code(self, code: str) -> dict[str, Any]:
        """Exchange an auth code for access + refresh tokens."""
        resp = await self.client.post(
            f"{_auth_url()}/connect/token",
            data={
                "grant_type": "authorization_code",
                "client_id": settings.truelayer_client_id,
                "client_secret": settings.truelayer_client_secret,
                "redirect_uri": settings.truelayer_redirect_uri,
                "code": code,
            },
        )
        resp.raise_for_status()
        return resp.json()

    async def refresh_access_token(self, refresh_token: str) -> dict[str, Any]:
        """Refresh an expired access token."""
        resp = await self.client.post(
            f"{_auth_url()}/connect/token",
            data={
                "grant_type": "refresh_token",
                "client_id": settings.truelayer_client_id,
                "client_secret": settings.truelayer_client_secret,
                "refresh_token": refresh_token,
            },
        )
        resp.raise_for_status()
        return resp.json()

    async def get_accounts(self, access_token: str) -> list[dict[str, Any]]:
        """List all connected bank accounts."""
        resp = await self.client.get(
            f"{_api_url()}/data/v1/accounts",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        resp.raise_for_status()
        return resp.json().get("results", [])

    async def get_transactions(
        self,
        access_token: str,
        account_id: str,
        from_date: datetime | None = None,
        to_date: datetime | None = None,
    ) -> list[dict[str, Any]]:
        """Fetch transactions for a specific account.

        Defaults to the last 90 days if no date range is provided.
        """
        if to_date is None:
            to_date = datetime.utcnow()
        if from_date is None:
            from_date = to_date - timedelta(days=90)

        params = {
            "from": from_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to": to_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        resp = await self.client.get(
            f"{_api_url()}/data/v1/accounts/{account_id}/transactions",
            headers={"Authorization": f"Bearer {access_token}"},
            params=params,
        )
        resp.raise_for_status()
        return resp.json().get("results", [])

    async def get_balance(self, access_token: str, account_id: str) -> dict[str, Any]:
        """Get current balance for an account."""
        resp = await self.client.get(
            f"{_api_url()}/data/v1/accounts/{account_id}/balance",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
        return results[0] if results else {}


truelayer_client = TrueLayerClient()
