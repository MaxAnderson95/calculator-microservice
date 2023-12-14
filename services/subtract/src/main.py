import time
import logging
import uvicorn
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from config import settings

logging.basicConfig(level=settings.LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Subtract Service")


class SubtractRequest(BaseModel):
    num1: float
    num2: float


class SubtractResponse(BaseModel):
    result: float


def subtract_controller(num1: float, num2: float) -> float:
    logger.info(f"Subtracting {num1} - {num2}")
    num2 = -num2
    time.sleep(2)
    logger.info(f"Sending request to add service: {num1} + {num2}")
    result = requests.post(
        f"{settings.ADD_SERVICE_URL}/api/v1/add", json={"num1": num1, "num2": num2}
    )
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise Exception(f"Received bad status code from add service: {e}")
    return result.json().get("result")


@app.post("/api/v1/subtract", response_model=SubtractResponse)
def subtract(request: SubtractRequest) -> SubtractResponse:
    logger.debug(f"Received request: {request}")
    result = subtract_controller(request.num1, request.num2)
    logger.debug(f"Returning result: {result}")
    return SubtractResponse(result=result)


if __name__ == "__main__":
    logger.debug(f"Starting server on port {settings.PORT} with DEBUG={settings.DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)
