import logging

from casper.file_ops import (
    valid_input_file,
    valid_workable_file,
)

from . import test_file_paths

module_logger = logging.getLogger(__name__)


def test_valid_workable_file():
    for path_to_test_data_file in test_file_paths:
        assert valid_workable_file(path_to_test_data_file)


def test_valid_input_file():
    for path_to_test_data_file in test_file_paths:
        assert valid_input_file(path_to_test_data_file)
