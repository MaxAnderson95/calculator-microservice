import logging
from venv import logger
from db import Session, CalculationLogEntry

logger = logging.getLogger(__name__)


def new_calculation_log(operation: str, num1: float, num2: float, result: float, cache_hit: bool) -> None:
    logger.info(f"Saving calculation log for operation: {operation} with values: {num1} and {num2}")
    with Session() as db:
        db.add(CalculationLogEntry(operation=operation, num1=num1, num2=num2, result=result, cache_hit=cache_hit))
        db.commit()
