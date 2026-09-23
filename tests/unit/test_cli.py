import os
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

import casper.cli

from .. import data_for_tests_dir


def test_cli():
    fname = str(
        data_for_tests_dir
        / "unit-test-data"
        / "TEMPO_NO2_L2_V04_20250917T215552Z_S012G09_subsetted.nc"
    )

    test_args = [
        casper.cli.__file__,
        fname,
    ]

    with TemporaryDirectory() as temp_dir, patch.object(sys, "argv", test_args):
        os.chdir(temp_dir)
        casper.cli.main()
