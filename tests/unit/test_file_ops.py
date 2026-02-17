import logging
from pathlib import Path
import pytest
import netCDF4 as nc

from casper.file_ops import (
    valid_workable_file,
    valid_input_file,
)

from .. import data_for_tests_dir
from ..conftest import path_str
 
module_logger = logging.getLogger(__name__)

def test_valid_workable_file():
    path_to_test_data_file = str(
        data_for_tests_dir / "unit-test-data" / "TEMPO_HCHO_L3_V04_20250912T210435Z_S012_subsetted.nc4"
    )

    assert valid_workable_file(path_to_test_data_file)

def test_valid_input_file():
    path_to_test_data_file = str(
        data_for_tests_dir / "unit-test-data" / "TEMPO_HCHO_L3_V04_20250912T210435Z_S012_subsetted.nc4"
    )
    assert valid_input_file(path_to_test_data_file)   
