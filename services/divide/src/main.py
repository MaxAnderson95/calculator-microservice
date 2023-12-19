import logging
import time
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import settings
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(level=settings.LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Divide Service")
instrumentator = Instrumentator().instrument(app)


class DivideRequest(BaseModel):
    num1: float
    num2: float


class DivideResponse(BaseModel):
    result: float


def divide_controller(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} / {num2}")
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    time.sleep(2)
    return num1 / num2


@app.post("/api/v1/divide", response_model=DivideResponse)
def divide(request: DivideRequest) -> DivideResponse:
    logger.debug(f"Received request: {request}")
    try:
        result = divide_controller(request.num1, request.num2)
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    logger.debug(f"Returning result: {result}")
    return DivideResponse(result=result)


instrumentator.expose(app)


if __name__ == "__main__":
    logger.debug(f"Starting server on port {settings.PORT} with DEBUG={settings.DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)
