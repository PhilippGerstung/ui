import redis
from loguru import logger

from external.environ import USE_FAKE_REDIS, REDIS_URL, REDIS_PORT, REDIS_PASSWORD

if USE_FAKE_REDIS:
    import fakeredis
    logger.info("Using fake redis")
    redis_db = fakeredis.FakeRedis()
else:
    logger.info("Using real redis")
    redis_db = redis.Redis(host=REDIS_URL, port=REDIS_PORT, db=0, password=REDIS_PASSWORD)
