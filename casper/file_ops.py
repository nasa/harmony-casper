"""File operation functions."""

from __future__ import annotations

import logging
from logging import Logger
from pathlib import Path

import numpy as np
import xarray as xr

module_logger = logging.getLogger(__name__)

# Module constants
VALID_EXTENSIONS = [".h5", ".nc", ".nc4", ".netcdf"]


def valid_workable_file(filename: str, logger: Logger = module_logger) -> bool:
    """
    Verify file is a valid non-empty netCDF files.

    Returns
    -------
    Boolean
        True if valid file that can be converted

    """
    try:
        with xr.open_datatree(filename) as dt:
            if not _is_file_empty(dt):
                logger.debug("File is valid and non-empty: %s", filename)
            else:
                logger.debug("File is empty: %s", filename)
        return True
    except Exception as e:
        logger.debug("Error opening %s: %s", filename, e)
        return False


def valid_input_file(filename: str) -> bool:
    """
    Verify valid filename specified

    Parameters
    ----------
    filename
       Name of file to be converted

    Returns
    -------
    Boolean
        True if filename valid. False if not

    Raises
    ------
    ValueError
        If filename not valid
    """
    module_logger.debug("Validating input file: %s", filename)

    if not filename:
        raise ValueError("No input file provided")

    # Single path - could be file or directory
    path = Path(filename).resolve()

    if path.is_dir():
        raise ValueError("Input must be a single filename")

    if path.is_file():
        if path.suffix.lower() in VALID_EXTENSIONS:
            return True
        else:
            raise ValueError("Input file must be a netcdf file")

    raise ValueError(f"Input path '{path}' is not a valid file")


def _is_file_empty(dt: xr.DataTree) -> bool:
    """Check if xarray datatree is empty.

    A dataset is considered empty if all variables are:
    1. Zero size, OR
    2. All masked values (for masked arrays), OR
    3. All fill values, OR
    4. All NaN values

    Parameters
    ----------
    parent_group
        netCDF dataset or group to check

    Returns
    -------
    bool
        True if dataset is empty, False if any variable contains data
    """
    for node in dt.subtree:
        if node.data_vars:
            # Loop through all variables inside the current group
            for _, ds in node.data_vars.items():
                if ds.size == 0:
                    continue  # Empty variable, check next one

                # Check if variable is non-empty using three different methods
                # Check 1: Are all values masked?
                var_data = ds.values

                if np.ma.isMaskedArray(var_data) and (
                    not var_data.mask.all() and not np.all(np.isnan(var_data.data))
                ):
                    return False  # Found a non-empty masked array

                # Check 2: Are all values equal to fill value?
                # Check 3: Are all values NaN?
                fill_val = ds.encoding.get("_FillValue", np.nan)
                all_fill_val = bool((ds == fill_val).all())
                all_nan = bool(ds.isnull().all())

                if not all_nan and not all_fill_val:
                    return False  # Found a non-empty variable

    # Check all child groups recursively, and return True if all variables and groups are empty.
    return all(_is_file_empty(child_group) for child_group in dt.groups.values())
