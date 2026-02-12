import json
from pathlib import Path
from .logger import logger

class FileService:
    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.filepath.parent.mkdir(exist_ok=True)

    def read_json(self):
        if not self.filepath.exists():
            logger.warning("File not found. Creating new file.")
            return []

        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            logger.error("JSON corrupted. Resetting file.")
            return []

    def write_json(self, data):
        try:
            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=2)
            logger.info("Data written successfully.")
        except Exception as e:
            logger.error(f"Write failed: {e}")
