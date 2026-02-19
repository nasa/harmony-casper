import os
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

import casper.cli

from .. import data_for_tests_dir


def test_cli():
    fname = str(
        data_for_tests_dir / "unit-test-data" / "TEMPO_HCHO_L3_V04_20250912T210435Z_S012_subsetted.nc4"
    )

    test_args = [
        casper.cli.__file__,
        fname,
    ]

    with TemporaryDirectory() as temp_dir, patch.object(sys, "argv", test_args):
        os.chdir(temp_dir)
        casper.cli.main()
