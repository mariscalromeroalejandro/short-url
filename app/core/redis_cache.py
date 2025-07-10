from aiocache import Cache
from aiocache.serializers import JsonSerializer
import os

# Redis DB 1 → para caché de URLs
default_cache = Cache(
    Cache.REDIS,
    endpoint=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    db=os.getenv('REDIS_CACHE_DB'),
    serializer=JsonSerializer(),
    ttl=os.getenv('REDIS_CACHE_TTL')
)
