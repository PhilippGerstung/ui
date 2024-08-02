import json
from functools import wraps

from loguru import logger
from pydantic import BaseModel

from external.redis import redis_db


def redis_cache(ttl: int, cachekey: callable):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key = "redis_cache_" + cachekey(*args, **kwargs)
            cached_result = redis_db.get(key)
            if cached_result:
                logger.debug(f"Cache hit for {key}")
                return json.loads(cached_result)
            logger.debug(f"Cache miss for {key}")
            result = await func(*args, **kwargs)

            if isinstance(result, BaseModel):
                serialized = result.model_dump_json()
            else:
                serialized = json.dumps(result)

            redis_db.set(key, serialized)
            redis_db.expire(key, ttl)
            return result

        return wrapper

    return decorator
