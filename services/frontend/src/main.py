import logging
import pathlib
import uvicorn
from typing import Annotated
from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from config import settings
import controller

logging.basicConfig(level=settings.LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Frontend Service")


@app.post("/api/v1/calculate")
def add(operation: Annotated[str, Form()], num1: Annotated[float, Form()], num2: Annotated[float, Form()]) -> float:
    logger.info(f"Received operation: {operation} with values: {num1} and {num2}")
    match operation:
        case "add":
            try:
                return controller.add(num1, num2)
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        case "subtract":
            try:
                return controller.subtract(num1, num2)
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        case "multiply":
            try:
                return controller.multiply(num1, num2)
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        case "divide":
            try:
                return controller.divide(num1, num2)
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))
        case _:
            raise HTTPException(status_code=404, detail="Invalid operation")


static_folder = pathlib.Path(__file__).parent.resolve() / "static"
app.mount("/", StaticFiles(directory=static_folder, html=True), name="static")

if __name__ == "__main__":
    logger.debug(f"Starting server on port {settings.PORT} with DEBUG={settings.DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)
