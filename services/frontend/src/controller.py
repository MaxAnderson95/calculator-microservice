import requests
import logging
from typing import Tuple
from config import settings
from cache import get_cache, set_cache

logger = logging.getLogger(__name__)


class CalculatorError(Exception):
    pass


op_to_svc = {
    "add": settings.ADD_SERVICE_URL,
    "subtract": settings.SUBTRACT_SERVICE_URL,
    "multiply": settings.MULTIPLY_SERVICE_URL,
    "divide": settings.DIVIDE_SERVICE_URL,
}


def calculate(operation: str, num1: float, num2: float) -> Tuple[float, bool]:
    cached_result = get_cache(operation, num1, num2)
    if cached_result is not None:
        return cached_result, True

    calc_result = requests.post(
        f"{op_to_svc[operation]}/api/v1/{operation}", json={"operation": operation, "num1": num1, "num2": num2}
    )

    try:
        calc_result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logger.error(e)
        if hasattr(e.response, "json"):
            raise CalculatorError(e.response.json().get("detail", "Unknown error"))
        else:
            raise CalculatorError("Unknown error")

    result = calc_result.json().get("result")
    set_cache(operation, num1, num2, result)
    return result, False
