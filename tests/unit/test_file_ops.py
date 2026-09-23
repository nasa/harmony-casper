import logging

from casper.file_ops import (
    valid_input_file,
    valid_workable_file,
)

from .. import data_for_tests_dir

module_logger = logging.getLogger(__name__)


def test_valid_workable_file():
    path_to_test_data_file = str(
        data_for_tests_dir
        / "unit-test-data"
        / "TEMPO_NO2_L2_V04_20250917T215552Z_S012G09_subsetted.nc"
    )

    assert valid_workable_file(path_to_test_data_file)


def test_valid_input_file():
    path_to_test_data_file = str(
        data_for_tests_dir
        / "unit-test-data"
        / "TEMPO_NO2_L2_V04_20250917T215552Z_S012G09_subsetted.nc"
    )
    assert valid_input_file(path_to_test_data_file)
