"""File operation functions."""

from __future__ import annotations

import logging
from logging import Logger
from pathlib import Path

import netCDF4 as nc
import numpy as np

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
        with nc.Dataset(filename, "r") as dataset:
            if not _is_file_empty(dataset):
                logger.debug("File is valid and non-empty: %s", filename)
            else:
                logger.debug("File is empty: %s", filename)
        return True
    except Exception as e:
        logger.debug("Error opening %s as netCDF: %s", filename, e)
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
    module_logger.debug("Validating input file: %s",filename)

    if not filename:
        raise ValueError("No input file provided")

    # Single path - could be file or directory
    path = Path(filename).resolve()

    if path.is_dir():
         raise ValueError("Input must be a single filename")

    if path.is_file():
        if path.suffix.lower() in VALID_EXTENSIONS:
            return str(path)
        else:
            raise ValueError("Input file must be a netcdf file")

    raise ValueError(f"Input path '{path}' is not a valid file")


def _is_file_empty(dataset: nc.Dataset | nc.Group) -> bool:
    """Check if netCDF dataset is empty.

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
    for _var_name, var in dataset.variables.items():
        if var.size == 0:
            continue  # Empty variable, check next one

        # Get fill value if defined
        fill_or_null = (
            getattr(var, "_FillValue", np.nan) if "_FillValue" in var.ncattrs() else np.nan
        )

        # Load the data
        var_data = var[:]

        # Check if variable is non-empty using three different methods
        # Check 1: Are all values masked?
        if np.ma.isMaskedArray(var_data) and (
                not var_data.mask.all() and not np.all(np.isnan(var_data.data))):
            return False  # Found a non-empty masked array

        # Check 2: Are all values equal to fill value?
        # Check 3: Are all values NaN?
        if not np.all(var_data.data == fill_or_null) and not np.all(np.isnan(var_data.data)):
            return False  # Found a non-empty variable

    # Check all child groups recursively, and return True if all variables and groups are empty.
    return all(_is_file_empty(child_group) for child_group in dataset.groups.values())
