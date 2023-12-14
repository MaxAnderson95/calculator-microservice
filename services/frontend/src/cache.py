import logging
from redis import Redis, RedisError
from config import settings

logger = logging.getLogger(__name__)
redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)


def get_cache(operation: str, num1: float, num2: float) -> float | None:
    try:
        value = redis.get(f"{operation}:{num1}:{num2}")
        if value is None and operation in ["add", "multiply"]:
            value = redis.get(f"{operation}:{num2}:{num1}")
    except RedisError as e:
        logger.warning(f"Cache miss due to Redis error: {e}")
        return None

    if value is None:
        logger.info(f"Cache miss for key: {operation}:{num1}:{num2}")
        return None
    else:
        logger.info(f"Cache hit for key: {operation}:{num1}:{num2}")
    return float(value)  # type: ignore


def set_cache(operation: str, num1: float, num2: float, val: float) -> None:
    try:
        redis.set(f"{operation}:{num1}:{num2}", val)
        logger.info(f"Caching result for key: {operation}:{num1}:{num2} to value: {val}")
    except RedisError as e:
        logger.warning(f"Failed to set cache due to Redis error: {e}")
