import logging
import time
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from config import settings
from prometheus_fastapi_instrumentator import Instrumentator

logging.basicConfig(level=settings.LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Add Service")
instrumentator = Instrumentator().instrument(app)


class AddRequest(BaseModel):
    num1: float
    num2: float


class AddResponse(BaseModel):
    result: float


def add_controller(num1: float, num2: float) -> float:
    logger.info(f"Adding {num1} + {num2}")
    time.sleep(2)
    return num1 + num2


@app.post("/api/v1/add", response_model=AddResponse)
def add(request: AddRequest) -> AddResponse:
    logger.debug(f"Received request: {request}")
    result = add_controller(request.num1, request.num2)
    logger.debug(f"Returning result: {result}")
    return AddResponse(result=result)


instrumentator.expose(app)

if __name__ == "__main__":
    logger.debug(f"Starting server on port {settings.PORT} with DEBUG={settings.DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)
