
"""A Harmony CLI wrapper around casper"""

import logging
import sys

from casper.convert_to_csv import convert_to_csv
from casper.file_ops import (
    valid_input_file,
    valid_workable_file,
)


def run_casper(input_file: str):
    """Parse arguments and run casper on specified input file."""
    if not valid_input_file(input_file):
            raise ValueError("Input filename not valid")

    if not valid_workable_file(input_file):
            raise ValueError("Input file not valid")
    zip_file_name = f"{input_file.split('/')[-1].split('.')[0]}.zip"
    convert_to_csv(input_file, zip_file_name)

def main() -> None:
    """Entry point for the casper command line tool."""
    logging.basicConfig(
        stream=sys.stdout,
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    run_casper(sys.argv[1])

if __name__ == "__main__":
    main()
