"""Validate text-bearing NetCDF files through the real file and CLI paths."""

import csv
import io
import subprocess
import sys
from zipfile import ZipFile

import numpy as np
import pytest
from netCDF4 import Dataset

from casper.file_ops import _is_file_empty, valid_workable_file


@pytest.mark.parametrize("kind", ["vlen", "char"])
@pytest.mark.parametrize("nested", [False, True])
def test_string_variables_are_valid_nonempty_files(tmp_path, kind, nested):
    path = tmp_path / "strings.nc"
    with Dataset(path, "w") as root:
        group = root.createGroup("details") if nested else root
        group.createDimension("row", 2)
        if kind == "vlen":
            text = group.createVariable("station", str, ("row",))
            text[:] = np.array(["alpha", "beta"], dtype=object)
        else:
            group.createDimension("character", 2)
            text = group.createVariable("station", "S1", ("row", "character"))
            text[:] = np.asarray(["ab", "cd"], dtype="S2").view("S1").reshape(2, 2)
    assert valid_workable_file(str(path))
    with Dataset(path) as dataset:
        assert not _is_file_empty(dataset)


@pytest.mark.parametrize("filled", [False, True])
def test_masked_character_variables_keep_missing_value_semantics(tmp_path, filled):
    path = tmp_path / "characters.nc"
    with Dataset(path, "w") as root:
        root.createDimension("row", 2)
        text = root.createVariable("station", "S1", ("row",), fill_value=b"_")
        if filled:
            text[1] = b"A"
    with Dataset(path) as dataset:
        assert _is_file_empty(dataset) is not filled
    assert valid_workable_file(str(path))


@pytest.mark.parametrize("kind", ["vlen", "char"])
def test_zero_size_text_variables_remain_empty(tmp_path, kind):
    path = tmp_path / "empty.nc"
    with Dataset(path, "w") as root:
        root.createDimension("row", None)
        root.createVariable("station", str if kind == "vlen" else "S1", ("row",))
    with Dataset(path) as dataset:
        assert _is_file_empty(dataset)


@pytest.mark.parametrize("values, empty", [([1.0, 2.0], False), ([np.nan, np.nan], True)])
def test_numeric_file_validation_is_unchanged(tmp_path, values, empty):
    path = tmp_path / "numbers.nc"
    with Dataset(path, "w") as root:
        root.createDimension("row", 2)
        root.createVariable("value", "f8", ("row",))[:] = values
    assert valid_workable_file(str(path))
    with Dataset(path) as dataset:
        assert _is_file_empty(dataset) is empty


def test_malformed_file_is_still_rejected(tmp_path):
    path = tmp_path / "invalid.nc"
    path.write_text("not a NetCDF file")
    assert not valid_workable_file(str(path))
    assert not valid_workable_file(str(tmp_path / "missing.nc"))


@pytest.mark.parametrize("nested", [False, True])
def test_cli_converts_string_first_files_without_losing_data(tmp_path, nested):
    path = tmp_path / "stations.nc"
    with Dataset(path, "w") as root:
        group = root.createGroup("details") if nested else root
        group.createDimension("row", 3)
        # Declare strings first so validation reaches the text variable before numbers.
        group.createVariable("station", str, ("row",))[:] = np.array(
            ["alpha", "bêta", "gamma"], dtype=object
        )
        group.createVariable("row", "i4", ("row",))[:] = [0, 1, 2]
        group.createVariable("measurement", "f8", ("row",))[:] = [1.0, np.nan, 3.0]
    subprocess.run(
        [sys.executable, "-m", "casper.cli", str(path)],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    with ZipFile(tmp_path / "stations.zip") as output:
        csv_files = [name for name in output.namelist() if name.endswith(".csv")]
        assert len(csv_files) == 1
        rows = list(csv.DictReader(io.StringIO(output.read(csv_files[0]).decode("utf-8"))))
        prefix = "/details" if nested else ""
        assert [row[prefix + "/station"] for row in rows] == ["alpha", "bêta", "gamma"]
        assert [row[prefix + "/measurement"] for row in rows] == ["1.0", "", "3.0"]
        assert "Readme.json" in output.namelist()
    with Dataset(path) as original:
        group = original["details"] if nested else original
        assert list(group["station"][:]) == ["alpha", "bêta", "gamma"]
