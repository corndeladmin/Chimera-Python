#!/usr/bin/env python3
import argparse
import sys
import time

from src.constants import LOG_FILE_DIRECTORY
from src.app import app

VERSION = "0.0.1"

# Helper function for command-line argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description=f'Logs are generated under {LOG_FILE_DIRECTORY}')
    parser.add_argument("-d", "--debug", action="store_true", help="Prints all options to console")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose logging messages")
    parser.add_argument("-i", type=str, help="Specify the input file (will default to test data without)")
    parser.add_argument("-o", type=str, help="Specify the output file (will default to console without)")
    parser.add_argument("-t", action="store_true", help="Use test data - will ignore any input file if set")
    parser.add_argument("--dataset-name", type=str, help="Specify the name of the dataset (will generate a random one if not provided)")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppresses output to the screen")
    parser.add_argument("-r", action="store_true", help="Save the output to Redis")
    parser.add_argument("-m", type=float, help="Sets a lower bound filter for magnitude")
    parser.add_argument("-M", type=float, help="Sets a higher bound filter for magnitude")
    parser.add_argument("-y", type=int, help="Sets the x origin")
    parser.add_argument("-x", type=int, help="Sets the y origin")
    parser.add_argument("-z", type=int, help="Sets the zoom level")
    parser.add_argument("-H", action="store_true", help="Prints a hello world message and exits")
    return parser.parse_args()

# Load dataset using load_data module
def main():
    options = parse_args()

    # Handle trivial cases
    if options.H:
        print("Hello, world!")
        sys.exit()

    # Hand off majority of functionality to app
    app(options)

    # Needed to give time to the logger to write out any pending logs
    time.sleep(1)

if __name__ == "__main__":
    main()
