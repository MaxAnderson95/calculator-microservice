import os
import logging

ADD_SERVICE_URL = os.environ.get("ADD_SERVICE_URL")
if not ADD_SERVICE_URL:
    raise ValueError("No ADD_SERVICE_URL environment variable set")

SUBTRACT_SERVICE_URL = os.environ.get("SUBTRACT_SERVICE_URL")
if not SUBTRACT_SERVICE_URL:
    raise ValueError("No SUBTRACT_SERVICE_URL environment variable set")

MULTIPLY_SERVICE_URL = os.environ.get("MULTIPLY_SERVICE_URL")
if not MULTIPLY_SERVICE_URL:
    raise ValueError("No MULTIPLY_SERVICE_URL environment variable set")

DIVIDE_SERVICE_URL = os.environ.get("DIVIDE_SERVICE_URL")
if not DIVIDE_SERVICE_URL:
    raise ValueError("No DIVIDE_SERVICE_URL environment variable set")

PORT = int(os.environ.get("PORT", 8000))
if not PORT:
    raise ValueError("No PORT environment variable set")

DEBUG = True if os.getenv("DEBUG") else False
LEVEL = logging.DEBUG if os.getenv("DEBUG") else logging.INFO
