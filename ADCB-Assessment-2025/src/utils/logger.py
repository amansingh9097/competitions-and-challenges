import sys
from loguru import logger

logger.add(
    "logs/app_{time:YYYY-MM-DD}.log",
    rotation="1 day",
    retention="10 days",
    compression="zip",
    level="DEBUG",
    format="{time} | {level} | {message}"
)

logger.success("Application started!")
logger.info("Application logger initialized!")