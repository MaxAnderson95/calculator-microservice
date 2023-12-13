import os
import logging
import pathlib
import uvicorn
from typing import Annotated
from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
import controller

LEVEL = logging.DEBUG if os.getenv("DEBUG") else logging.INFO
logging.basicConfig(level=LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Frontend Service")


@app.post("/api/v1/add")
def add(num1: Annotated[float, Form()], num2: Annotated[float, Form()]) -> float:
    logger.info(f"Adding {num1} + {num2}")
    return controller.add(num1, num2)


@app.post("/api/v1/subtract")
def subtract(num1: Annotated[float, Form()], num2: Annotated[float, Form()]) -> float:
    logger.info(f"Subtracting {num1} - {num2}")
    return controller.subtract(num1, num2)


@app.post("/api/v1/multiply")
def multiply(num1: Annotated[float, Form()], num2: Annotated[float, Form()]) -> float:
    logger.info(f"Multiplying {num1} * {num2}")
    return controller.multiply(num1, num2)


@app.post("/api/v1/divide")
def divide(num1: Annotated[float, Form()], num2: Annotated[float, Form()]) -> float:
    logger.info(f"Dividing {num1} / {num2}")
    try:
        return controller.divide(num1, num2)
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))


static_folder = pathlib.Path(__file__).parent.resolve() / "static"
app.mount("/", StaticFiles(directory=static_folder, html=True), name="static")

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = True if os.getenv("DEBUG") else False
    logger.debug(f"Starting server on port {PORT} with DEBUG={DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=DEBUG)
