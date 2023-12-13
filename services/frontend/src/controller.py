import requests
import config


def add(num1: float, num2: float) -> float:
    result = requests.post(
        f"{config.ADD_SERVICE_URL}/api/v1/add", json={"num1": num1, "num2": num2}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.json().get("detail", "Unknown error"))
    return result.json().get("result")


def subtract(num1: float, num2: float) -> float:
    result = requests.post(
        f"{config.SUBTRACT_SERVICE_URL}/api/v1/subtract", json={"num1": num1, "num2": num2}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.json().get("detail", "Unknown error"))
    return result.json().get("result")


def multiply(num1: float, num2: float) -> float:
    result = requests.post(
        f"{config.MULTIPLY_SERVICE_URL}/api/v1/multiply", json={"num1": num1, "num2": num2}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.json().get("detail", "Unknown error"))
    return result.json().get("result")


def divide(num1: float, num2: float) -> float:
    result = requests.post(
        f"{config.DIVIDE_SERVICE_URL}/api/v1/divide", json={"num1": num1, "num2": num2}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(e.response.json().get("detail", "Unknown error"))
    return result.json().get("result")
