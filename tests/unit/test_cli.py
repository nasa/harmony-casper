import os
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

import casper.cli

from . import test_file_paths


def test_cli():
    for fname in test_file_paths:
        test_args = [
            casper.cli.__file__,
            fname,
        ]

        with TemporaryDirectory() as temp_dir, patch.object(sys, "argv", test_args):
            os.chdir(temp_dir)
            casper.cli.main()
