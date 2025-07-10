import os
import logging

from aiocache import caches
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler

from app.db import create_db_and_tables
from app.api.urls import api_router, public_router
from app.handlers.exception_handlers import add_exception_handlers
from app.services.write_service import delete_expired_urls



# ---------------------------
# Redis Cache Configuration
# ---------------------------
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


# ---------------------------
# Logger Configuration
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)
logger = logging.getLogger(__name__)


# ---------------------------
# Lifespan Context Manager for DB Initialization
# ---------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan context manager.

    - Initializes database tables before the app starts.
    - Logs success or failure.
    - Raises exception to stop app startup if DB init fails.
    """
    try:
        create_db_and_tables()  # Synchronous function called directly
        logger.info("Database tables created successfully.")
        yield
    except Exception as e:
        logger.error(f"Failed to create database tables: {e}", exc_info=True)
        raise  # Stop FastAPI startup on DB init failure


# ---------------------------
# Create FastAPI app instance
# ---------------------------
app = FastAPI(lifespan=lifespan)


# ---------------------------
# Middleware
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)


# ---------------------------
# Routes and Exception Handlers
# ---------------------------
add_exception_handlers(app)

app.include_router(api_router, prefix="/api", tags=["URL Shortener"])
app.include_router(public_router)

# ----------------------------
# Background Scheduler
# ----------------------------
scheduler = BackgroundScheduler()
scheduler.add_job(delete_expired_urls, 'interval', minutes=1)
scheduler.start()