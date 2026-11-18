import logging
from os import listdir, makedirs
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from casper.convert_to_csv import (
    convert_to_csv,
)

from . import test_file_paths

module_logger = logging.getLogger(__name__)


def test_coversion():

    with TemporaryDirectory() as temp_dir:
        for fname in test_file_paths:
            test_data_dir = fname.rsplit("/", 1)[0]
            csv_test_files = sorted([f for f in listdir(test_data_dir) if "csv" in f])
            num_csv_test_files = len(csv_test_files)

            # Convert test file to CSVs
            output_dir = f"{temp_dir}/{fname.split('/')[-2]}"
            makedirs(output_dir, exist_ok=True)
            zip_file = f"{output_dir}/{fname.rsplit('/', 1)[-1].replace('.nc', '.zip')}"
            num_csv_files = convert_to_csv(
                fname,
                zip_file,
                logger=module_logger,
            )
            assert num_csv_files == num_csv_test_files
            # Extract converted files and compare to test files in unit-test-data
            with ZipFile(zip_file, "r") as zip_ref:
                zip_ref.extractall(output_dir)
            op_files = sorted(
                [f.split("/")[-1] for f in listdir(f"{output_dir}") if "Readme" in f or "csv" in f]
            )
            test_files = sorted(
                [
                    f.split("/")[-1]
                    for f in listdir(f"{test_data_dir}")
                    if "Readme" in f or "csv" in f
                ]
            )
            assert op_files == test_files
            for f in test_files:
                f1 = Path(f"{output_dir}") / f"{f}"
                f2 = Path(f"{test_data_dir}") / f"{f}"
                assert f1.read_bytes() == f2.read_bytes()
