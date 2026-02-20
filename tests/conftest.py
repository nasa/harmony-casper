"""Initial configuration for tests."""

import typing
from pathlib import Path

test_path = Path(__file__).parents[0].resolve()
data_path = test_path.joinpath("data")


class DataDirs(typing.NamedTuple):
    test_path: Path
    test_data_path: Path


def path_str(dir_path: Path, filename: str) -> str:
    return str(dir_path.joinpath(filename))
