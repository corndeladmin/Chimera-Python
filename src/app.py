## src/app.py
from src.load_data import load_data
from src.filter import filter_data
from src.transform import transform_data
from src.output import output_data
from src.log_manager import get_log_manager

def app(options):
    logger = get_log_manager(options)
    logger.info("===========================================")
    logger.info("Start the process")

    # Load the data
    data = load_data(logger, options)
    logger.debug(f"Items found: {len(data)}")

    # Filter the data
    filtered_data = filter_data(logger, options, data)
    logger.debug(f"Items after filtering: {len(filtered_data)}")

    # Transform the data
    transformed_data = transform_data(logger, options, filtered_data)
    logger.debug(f"Items after transformation: {len(transformed_data)}")

    # Output the data
    output_data(logger, options, transformed_data)
    logger.info("Finishing the process")
    logger.info("Exiting. Bye!")
