import os
import logging
import uvicorn
from typing import Annotated
from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

LEVEL = logging.DEBUG if os.getenv("DEBUG") else logging.INFO
logging.basicConfig(level=LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Frontend Service")


@app.post("/api/v1/add")
def add(num1: Annotated[float, Form()], num2: Annotated[float, Form()]):
    logger.info(f"Adding {num1} + {num2}")
    result = num1 + num2
    return result


@app.post("/api/v1/subtract")
def subtract(num1: Annotated[float, Form()], num2: Annotated[float, Form()]):
    logger.info(f"Subtracting {num1} - {num2}")
    result = num1 - num2
    return result


@app.post("/api/v1/multiply")
def multiply(num1: Annotated[float, Form()], num2: Annotated[float, Form()]):
    logger.info(f"Multiplying {num1} * {num2}")
    result = num1 * num2
    return result


@app.post("/api/v1/divide")
def divide(num1: Annotated[float, Form()], num2: Annotated[float, Form()]):
    logger.info(f"Dividing {num1} / {num2}")
    if num2 == 0:
        logger.error("Cannot divide by zero")
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = num1 / num2
    return result


app.mount("/", StaticFiles(directory="./services/frontend/src/static", html=True), name="static")

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = True if os.getenv("DEBUG") else False
    logger.debug(f"Starting server on port {PORT} with DEBUG={DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=DEBUG)
