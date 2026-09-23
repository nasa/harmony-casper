import logging
from os import listdir
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from casper.convert_to_csv import (
    convert_to_csv,
)

from .. import data_for_tests_dir

module_logger = logging.getLogger(__name__)


def test_coversion():
    fname = str(
        data_for_tests_dir
        / "unit-test-data"
        / "TEMPO_NO2_L2_V04_20250917T215552Z_S012G09_subsetted.nc"
    )
    test_data_dir = str(data_for_tests_dir / "unit-test-data/")
    csv_test_files = sorted([f.split("/")[-1] for f in listdir(f"{test_data_dir}") if "csv" in f])
    num_csv_test_files = len(csv_test_files)
    with TemporaryDirectory() as temp_dir:
        zip_file_name = fname.split("/")[-1].split(".")[0]

        # Convert test file to CSVs
        zip_file = f"{temp_dir}/{zip_file_name}.zip"
        num_csv_files = convert_to_csv(
            fname,
            zip_file,
            logger=module_logger,
        )
        assert num_csv_files == num_csv_test_files
        # Extract converted files and compare to test files in unit-test-data
        with ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(temp_dir)
        op_files = sorted(
            [f.split("/")[-1] for f in listdir(f"{temp_dir}") if "Readme" in f or "csv" in f]
        )
        test_files = sorted(
            [f.split("/")[-1] for f in listdir(f"{test_data_dir}") if "Readme" in f or "csv" in f]
        )
        assert op_files == test_files
        for f in test_files:
            f1 = Path(f"{temp_dir}") / f"{f}"
            f2 = Path(f"{test_data_dir}") / f"{f}"
            assert f1.read_bytes() == f2.read_bytes()
