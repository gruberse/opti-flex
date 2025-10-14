import logging
import os
from datetime import datetime


def setup_logger():
    directory = './app/logger/logs'
    os.makedirs(directory, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{directory}/controller_{timestamp}.log'

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    logging.info('Starting the OptiFlex API.')


# Set up logging and create logger for this module
setup_logger()
logger = logging.getLogger(__name__)
