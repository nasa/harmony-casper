import sys
from unittest.mock import patch
import pytest
import casper.cli
from tempfile import TemporaryDirectory
from .. import data_for_tests_dir
from os import remove

def test_cli():
    fname = str(
        data_for_tests_dir / "unit-test-data" / "TEMPO_HCHO_L3_V04_20250912T210435Z_S012_subsetted.nc4"
    )

    test_args = [
        casper.cli.__file__,
        fname,
    ]

    f = 'TEMPO_HCHO_L3_V04_20250912T210435Z_S012_subsetted.zip'
    with TemporaryDirectory() as temp_dir:
        with patch.object(sys, "argv", test_args):
            casper.cli.main()
    remove(f)
