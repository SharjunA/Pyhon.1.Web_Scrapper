import logging

# Configure logging settings
logging.basicConfig(
    filename="logs/application.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)