import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok = True)

# Suppress TensorFlow logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Disable TensorFlow INFO logs
tensorflow_logger = logging.getLogger('tensorflow')
tensorflow_logger.setLevel(logging.ERROR)

# Configure logging settings
logging.basicConfig(
    filename = "logs/application.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)