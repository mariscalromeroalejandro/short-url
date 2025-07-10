from aiocache import cached, caches
from sqlmodel import Session, select
from app.db import engine
from app.models.UrlModel import Url
from app.exceptions import NotFoundUrl
from app.core.logging_config import logger
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

async def query_db(short_code: str):
    def db_query():
        try:
            with Session(engine) as session:
                statement = select(Url).where(Url.short_code == short_code)
                result = session.exec(statement).first()
                logger.debug(f"DB query result for {short_code}: {result}")
                return result
        except Exception as e:
            logger.error(f"Error querying DB for {short_code}: {e}", exc_info=True)
            return None
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, db_query)

def cache_key_builder(func, short_code, *args, **kwargs):
    return f"get_original_url:{short_code}"

@cached(ttl=60, key_builder=cache_key_builder)
async def get_original_url(short_code: str) -> str:
    try:
        logger.info(f"Cache MISS for short_code: {short_code}, querying DB")
        url = await query_db(short_code)
        if url:
            logger.info(f"Loaded long_url from DB: {url.long_url}")
            return url.long_url
        logger.warning(f"URL not found in DB for short_code: {short_code}")
        raise NotFoundUrl("URL not found")
    except NotFoundUrl as nf:
        logger.warning(f"NotFoundUrl exception: {nf}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in get_original_url: {e}", exc_info=True)
        raise
