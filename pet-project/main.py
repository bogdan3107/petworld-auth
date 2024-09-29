import logging
from contextlib import asynccontextmanager
from core.models import db_helper
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from logging_config import configure_logging
from api import router as api_router
from utils.timing import measure_time

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    logger.info("Starting lifespan")
    # startup
    yield
    # shutdown
    logger.info("Stopping lifespan")
    await db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

main_app.include_router(
    api_router,
)


@main_app.middleware("http")
@measure_time
async def process_request(request: Request, call_next):
    return await call_next(request)