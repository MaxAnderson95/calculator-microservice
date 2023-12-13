import os
import logging

ADD_SERVICE_URL = os.environ.get("ADD_SERVICE_URL")
if not ADD_SERVICE_URL:
    raise ValueError("No ADD_SERVICE_URL environment variable set")

PORT = int(os.environ.get("PORT", 8002))
if not PORT:
    raise ValueError("No PORT environment variable set")

DEBUG = True if os.getenv("DEBUG") else False
LEVEL = logging.DEBUG if os.getenv("DEBUG") else logging.INFO
