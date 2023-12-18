import logging
import pathlib
import uvicorn
import controller
from typing import Annotated
from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from config import settings, ALLOWED_OPERATIONS
from db_logging import new_calculation_log
from opentelemetry import trace

logging.basicConfig(level=settings.LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="Frontend Service")
tracer = trace.get_tracer(__name__)


@app.post("/api/v1/calculate")
def calculate(operation: Annotated[str, Form()], num1: Annotated[float, Form()], num2: Annotated[float, Form()]) -> float:
    with tracer.start_as_current_span("calculate") as span:
        logger.info(f"Received operation: {operation} with values: {num1} and {num2}")
        span.set_attribute("operation", operation)
        span.set_attribute("num1", num1)
        span.set_attribute("num2", num2)
        if operation not in ALLOWED_OPERATIONS:
            raise HTTPException(status_code=404, detail="Invalid operation")

        try:
            result, cache_hit = controller.calculate(operation, num1, num2)
            new_calculation_log(operation, num1, num2, result, cache_hit)
            return result
        except controller.CalculatorError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            logger.error(e)
            raise HTTPException(status_code=500, detail="An unknown error occurred")


static_folder = pathlib.Path(__file__).parent.resolve() / "static"
app.mount("/", StaticFiles(directory=static_folder, html=True), name="static")

if __name__ == "__main__":
    logger.debug(f"Starting server on port {settings.PORT} with DEBUG={settings.DEBUG}")
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)
