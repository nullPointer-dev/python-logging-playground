import logging
from pathlib import Path
from .config import BASE_DIR, LOG_LEVEL

log_path = BASE_DIR / "logs"
log_path.mkdir(exist_ok=True)

log_file = log_path / "app.log"

logging.basicConfig(
    filename=log_file,
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
