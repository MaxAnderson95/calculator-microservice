import os
import logging
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

LEVEL = logging.DEBUG if os.getenv("DEBUG") else logging.INFO
logging.basicConfig(level=LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Add Service")


class AddRequest(BaseModel):
    num1: float
    num2: float


class AddResponse(BaseModel):
    result: float


def add_controller(num1: float, num2: float) -> float:
    logger.info(f"Adding {num1} + {num2}")
    return num1 + num2


@app.post("/api/v1/add", response_model=AddResponse)
def add(request: AddRequest) -> AddResponse:
    logger.debug(f"Received request: {request}")
    result = add_controller(request.num1, request.num2)
    logger.debug(f"Returning result: {result}")
    return AddResponse(result=result)


if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8001))
    DEBUG = True if os.getenv("DEBUG") else False
    logger.debug(f"Starting server on port {PORT} with DEBUG={DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=DEBUG)
