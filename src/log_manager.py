## src/log_manager.py
import os
import logging

from src.constants import LOG_FILE_DIRECTORY

def get_log_manager(options):
    log_level = logging.DEBUG if options.verbose else logging.WARNING
    log_manager = logging.getLogger()
    log_manager.setLevel(log_level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    log_manager.addHandler(console_handler)

    # File handler
    if not os.path.exists(LOG_FILE_DIRECTORY):
        os.makedirs(LOG_FILE_DIRECTORY)
    file_handler = logging.FileHandler(f"{LOG_FILE_DIRECTORY}/cliapp.log")
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    log_manager.addHandler(file_handler)

    return log_manager

