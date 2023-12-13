def add(num1: float, num2: float) -> float:
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2
