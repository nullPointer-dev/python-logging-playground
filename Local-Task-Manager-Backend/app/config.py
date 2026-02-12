import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
DATA_FILE = BASE_DIR / os.getenv("DATA_FILE", "data/tasks.json")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

