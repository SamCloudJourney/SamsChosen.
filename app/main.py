"""FastAPI application entry point."""

import pathlib
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes import router
from app.api.demo import demo_router
from app.config import settings
from app.database import engine
from app.models.base import Base

STATIC_DIR = pathlib.Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Cleanup
    await engine.dispose()


app = FastAPI(
    title=settings.app_name,
    description="UK automated bookkeeping for freelancers & sole traders. MTD ITSA compliant.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(router, prefix="/api")
app.include_router(demo_router, prefix="/api/demo")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/health")
async def health():
    return {"status": "ok", "app": settings.app_name}


@app.get("/")
async def index():
    return FileResponse(str(STATIC_DIR / "index.html"))
