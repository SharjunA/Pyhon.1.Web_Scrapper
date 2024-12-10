import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging settings
logging.basicConfig(
    filename="logs/application.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)