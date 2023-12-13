import os
import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

LEVEL = logging.DEBUG if os.getenv("DEBUG") else logging.INFO
logging.basicConfig(level=LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Divide Service")


class DivideRequest(BaseModel):
    num1: float
    num2: float


class DivideResponse(BaseModel):
    result: float


def divide_controller(num1: float, num2: float) -> float:
    logger.info(f"Dividing {num1} * {num2}")
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
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


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8003))
    DEBUG = True if os.getenv("DEBUG") else False
    logger.debug(f"Starting server on port {PORT} with DEBUG={DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=DEBUG)
