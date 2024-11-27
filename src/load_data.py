## src/load_data.py
import os
import json
from src.convert_from_chi import convert_from_chi

TEST_DATA = [
    # Example test data here
    "45.0|93.0|Test Comment|3.0",
    "46.0|94.0|Another Comment|5.0"
]

def load_data(logger, options):
    logger.info("Loading data")
    if options.t:
        logger.info("Using test data")
        return convert_from_chi(logger, TEST_DATA)

    if not options.i:
        logger.info("No input file specified, returning empty data")
        return []

    try:
        with open(options.i, 'r') as file:
            lines = file.readlines()
            return convert_from_chi(logger, lines)
    except FileNotFoundError:
        logger.error(f"File {options.i} not found. Using test data.")
        return convert_from_chi(logger, TEST_DATA)
