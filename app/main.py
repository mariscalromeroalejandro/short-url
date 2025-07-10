from aiocache import caches
import os

caches.set_config({
    'default': {
        'cache': "aiocache.RedisCache",
        'endpoint': os.getenv('REDIS_HOST'),
        'port': os.getenv('REDIS_PORT'),
        'db': os.getenv('REDIS_CACHE_DB'),
        'serializer': {
            'class': "aiocache.serializers.JsonSerializer"
        },
        'ttl': os.getenv('REDIS_CACHE_TTL'),
    }
})




from fastapi import FastAPI
from app.db import create_db_and_tables
from contextlib import asynccontextmanager
import logging
from app.api.urls import api_router, public_router
from app.handlers.exception_handlers import add_exception_handlers
from fastapi.middleware.cors import CORSMiddleware



# Configurar logger con formato y nivel INFO
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for FastAPI lifespan.

    Initializes database tables before the app starts.
    Logs success or failure.

    If DB initialization fails, raises an exception to stop the app startup.
    """
    try:
        # create_db_and_tables() is synchronous, so call directly
        create_db_and_tables()
        logger.info("Database tables created successfully.")
        yield
    except Exception as e:
        logger.error(f"Failed to create database tables: {e}", exc_info=True)
        # Re-raise exception to stop FastAPI startup if DB init fails
        raise


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

add_exception_handlers(app)
app.include_router(api_router, prefix="/api", tags=["URL Shortener"])
app.include_router(public_router)