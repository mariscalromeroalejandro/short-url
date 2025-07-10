import redis
import os

redis_counter = redis.Redis(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    db=os.getenv('REDIS_COUNTER_DB'),
    decode_responses=True
)