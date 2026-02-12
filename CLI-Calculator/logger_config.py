import logging
from pathlib import Path

class SessionFilter(logging.Filter):
    def __init__(self, session_id):
        self.session_id = session_id
    
    def filter(self, record):
        record.session = self.session_id
        return True

base_dir = Path(__file__).resolve().parent
log_path = base_dir / "logfile.log"

def setup_logging(session_id):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    #FILE HANDLER
    file_handler = logging.FileHandler(log_path, mode = 'a')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("%(asctime)s | %(name)-10s | %(levelname)-8s | %(session)-12s | %(message)s")
    file_handler.setFormatter(file_formatter)

    #CONSOLE HANDLER
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    cosnole_formatter = logging.Formatter("%(levelname)-8s | %(message)s")
    console_handler.setFormatter(cosnole_formatter)

    #FILTER HANDLER
    session_filter = SessionFilter(session_id)
    file_handler.addFilter(session_filter)
    console_handler.addFilter(session_filter)

    if not logger.handlers: #Duplicate handler prevention
        #ATTACH HANDLERS
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

