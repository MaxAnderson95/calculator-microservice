import logging
from redis import Redis, RedisError
from config import settings

logger = logging.getLogger(__name__)
redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)


def get_cache(key: str) -> float | None:
    try:
        value = redis.get(key)
    except RedisError as e:
        logger.warning(f"Cache miss due to Redis error: {e}")
        return None

    if value is None:
        logger.info(f"Cache miss for key: {key}")
        return None
    else:
        logger.info(f"Cache hit for key: {key}")
    return float(value)  # type: ignore


def set_cache(key: str, val: float) -> None:
    try:
        redis.set(key, val)
        logger.info(f"Caching result for key: {key} to value: {val}")
    except RedisError as e:
        logger.warning(f"Failed to set cache due to Redis error: {e}")
