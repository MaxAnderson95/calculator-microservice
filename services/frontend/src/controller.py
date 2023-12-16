from typing import Tuple
import requests
from config import settings
from cache import get_cache, set_cache


def add(num1: float, num2: float) -> Tuple[float, bool]:
    cached_result = get_cache("add", num1, num2)
    if cached_result is not None:
        return cached_result, True
    add_result = requests.post(
        f"{settings.ADD_SERVICE_URL}/api/v1/add", json={"num1": num1, "num2": num2}
    )
    try:
        add_result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.json().get("detail", "Unknown error"))
    result = add_result.json().get("result")
    set_cache("add", num1, num2, result)
    return result, False


def subtract(num1: float, num2: float) -> Tuple[float, bool]:
    cached_result = get_cache("subtract", num1, num2)
    if cached_result is not None:
        return cached_result, True
    subtract_result = requests.post(
        f"{settings.SUBTRACT_SERVICE_URL}/api/v1/subtract", json={"num1": num1, "num2": num2}
    )
    try:
        subtract_result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.json().get("detail", "Unknown error"))
    result = subtract_result.json().get("result")
    set_cache("subtract", num1, num2, result)
    return result, False


def multiply(num1: float, num2: float) -> Tuple[float, bool]:
    cached_result = get_cache("multiply", num1, num2)
    if cached_result is not None:
        return cached_result, True
    multiply_result = requests.post(
        f"{settings.MULTIPLY_SERVICE_URL}/api/v1/multiply", json={"num1": num1, "num2": num2}
    )
    try:
        multiply_result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.json().get("detail", "Unknown error"))
    result = multiply_result.json().get("result")
    set_cache("multiply", num1, num2, result)
    return result, False


def divide(num1: float, num2: float) -> Tuple[float, bool]:
    cached_result = get_cache("divide", num1, num2)
    if cached_result is not None:
        return cached_result, True
    divide_result = requests.post(
        f"{settings.DIVIDE_SERVICE_URL}/api/v1/divide", json={"num1": num1, "num2": num2}
    )
    try:
        divide_result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.json().get("detail", "Unknown error"))
    result = divide_result.json().get("result")
    set_cache("divide", num1, num2, result)
    return result, False
