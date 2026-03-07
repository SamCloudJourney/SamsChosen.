"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    app_name: str = "SamsChosen Bookkeeper"
    debug: bool = False
    database_url: str = "sqlite+aiosqlite:///./bookkeeper.db"
    secret_key: str = "change-me-in-production"

    # TrueLayer (Open Banking)
    truelayer_client_id: str = ""
    truelayer_client_secret: str = ""
    truelayer_redirect_uri: str = "http://localhost:8000/api/banking/callback"
    truelayer_sandbox: bool = True

    # HMRC MTD
    hmrc_client_id: str = ""
    hmrc_client_secret: str = ""
    hmrc_redirect_uri: str = "http://localhost:8000/api/hmrc/callback"
    hmrc_sandbox: bool = True

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
