# app/core/logging_config.py
import logging

logger = logging.getLogger("cache_logger")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
