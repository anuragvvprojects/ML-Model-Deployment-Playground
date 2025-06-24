import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "local")
MODEL_PATH = os.getenv("MODEL_PATH", "model/artifacts/model.joblib")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
