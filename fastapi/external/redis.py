import fakeredis
import redis
from loguru import logger

from external.environ import USE_FAKE_REDIS

if USE_FAKE_REDIS:
    logger.info("Using fake redis")
    redis_db = fakeredis.FakeRedis()
else:
    logger.info("Using real redis")
    redis_db = redis.Redis(host="localhost", port=6379, db=0)
