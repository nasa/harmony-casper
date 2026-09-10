"""Scalar NetCDF variables should produce one-row CSV schemas."""

import csv
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from zipfile import ZipFile

import netCDF4 as nc
import numpy as np

from casper.convert_to_csv import convert_to_csv


class TestScalarConversion(TestCase):
    """Use real NetCDF files and inspect the generated archive contents."""

    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.input = Path(self.directory.name) / "scalars.nc"
        self.output = Path(self.directory.name) / "scalars.zip"

    def read_csvs(self):
        with ZipFile(self.output) as archive:
            csvs = {
                name: archive.read(name).decode("utf-8")
                for name in archive.namelist()
                if name.endswith(".csv")
            }
            metadata = json.loads(archive.read("Readme.json"))
            markdown = archive.read("Readme.md").decode("utf-8")
        return csvs, metadata, markdown

    def test_scalar_numeric_values_and_metadata(self):
        with nc.Dataset(self.input, "w") as dataset:
            dataset.title = "Scalar measurements"
            dataset.createVariable("temperature", "f8", ()).assignValue(273.15)
            dataset.createVariable("count", "i4", ()).assignValue(3)
        self.assertEqual(convert_to_csv(str(self.input), str(self.output)), 1)
        csvs, metadata, markdown = self.read_csvs()
        name, content = next(iter(csvs.items()))
        self.assertEqual(
            list(csv.DictReader(io.StringIO(content))), [{"/count": "3", "/temperature": "273.15"}]
        )
        self.assertEqual(metadata[name]["dimensions"], "")
        self.assertEqual(metadata[name]["variables"], ["/count", "/temperature"])
        self.assertIn("1 CSV files created", markdown)
        self.assertIn("Scalar measurements", markdown)

    def test_scalar_and_chunked_schemas_are_separate(self):
        with nc.Dataset(self.input, "w") as dataset:
            dataset.createVariable("offset", "f8", ()).assignValue(0.5)
            dataset.createDimension("sample", 23)
            dataset.createVariable("sample", "i4", ("sample",))[:] = np.arange(23)
            dataset.createVariable("signal", "f8", ("sample",))[:] = np.arange(23) * 2.0
        self.assertEqual(convert_to_csv(str(self.input), str(self.output)), 2)
        csvs, metadata, _ = self.read_csvs()
        scalar = next(name for name in csvs if metadata[name]["dimensions"] == "")
        vector = next(name for name in csvs if metadata[name]["dimensions"] == "sample")
        self.assertEqual(list(csv.DictReader(io.StringIO(csvs[scalar]))), [{"/offset": "0.5"}])
        rows = list(csv.DictReader(io.StringIO(csvs[vector])))
        self.assertEqual(len(rows), 23)
        self.assertEqual([float(row["/signal"]) for row in rows], list(np.arange(23) * 2.0))
        self.assertNotIn("/offset", rows[0])

    def test_scalar_names_in_groups_remain_distinct(self):
        with nc.Dataset(self.input, "w") as dataset:
            dataset.createVariable("value", "i4", ()).assignValue(1)
            group = dataset.createGroup("quality")
            group.description = "Group metadata"
            group.createVariable("value", "i4", ()).assignValue(2)
        self.assertEqual(convert_to_csv(str(self.input), str(self.output)), 1)
        csvs, metadata, markdown = self.read_csvs()
        content = next(iter(csvs.values()))
        self.assertEqual(
            list(csv.DictReader(io.StringIO(content))), [{"/quality/value": "2", "/value": "1"}]
        )
        self.assertIn("Group /quality Attributes:", metadata)
        self.assertIn("Group metadata", markdown)

    def test_missing_scalar_values_keep_header_only(self):
        with nc.Dataset(self.input, "w") as dataset:
            dataset.createVariable("missing", "f8", (), fill_value=-999.0)
        self.assertEqual(convert_to_csv(str(self.input), str(self.output)), 1)
        csvs, _, _ = self.read_csvs()
        content = next(iter(csvs.values()))
        self.assertEqual(list(csv.reader(io.StringIO(content))), [["/missing"]])

    def test_missing_value_does_not_drop_a_valid_scalar(self):
        with nc.Dataset(self.input, "w") as dataset:
            dataset.createVariable("missing", "f8", (), fill_value=-999.0)
            dataset.createVariable("valid", "f8", ()).assignValue(7.0)
        self.assertEqual(convert_to_csv(str(self.input), str(self.output)), 1)
        csvs, _, _ = self.read_csvs()
        self.assertEqual(
            list(csv.DictReader(io.StringIO(next(iter(csvs.values()))))),
            [{"/missing": "", "/valid": "7.0"}],
        )

    def test_scalar_strings_are_quoted_and_preserved(self):
        text = 'NASA, "café"\nnext line'
        with nc.Dataset(self.input, "w") as dataset:
            dataset.createVariable("label", str, ())[()] = text
            dataset.createVariable("count", "i4", ()).assignValue(3)
        self.assertEqual(convert_to_csv(str(self.input), str(self.output)), 1)
        csvs, _, _ = self.read_csvs()
        self.assertEqual(
            list(csv.DictReader(io.StringIO(next(iter(csvs.values()))))),
            [{"/count": "3", "/label": text}],
        )

    def test_scalar_time_coordinate_preserves_timestamp(self):
        with nc.Dataset(self.input, "w") as dataset:
            time = dataset.createVariable("observation_time", "i8", ())
            time.units = "seconds since 2026-01-01 00:00:00"
            time.assignValue(3600)
            value = dataset.createVariable("temperature", "f8", ())
            value.coordinates = "observation_time"
            value.assignValue(273.15)
        self.assertEqual(convert_to_csv(str(self.input), str(self.output)), 1)
        csvs, metadata, _ = self.read_csvs()
        name, content = next(iter(csvs.items()))
        self.assertEqual(
            list(csv.DictReader(io.StringIO(content))),
            [{"observation_time": "2026-01-01 01:00:00", "/temperature": "273.15"}],
        )
        self.assertEqual(metadata[name]["non-dimensional coordinates"], "observation_time")
