#!/usr/bin/env python
import xarray as xr
import sys
import logging
from logging import Logger
import zipfile
from harmony_service_lib.logging import build_logger
from casper.file_ops import valid_input_file, valid_workable_file

default_logger = logging.getLogger(__name__)

def convert_to_csv(fname:str, zip_file: str, logger: Logger = default_logger) -> int:
    """
    Converts NetCDF file to one or more CSV files. The number of files will
    be based on the dimensions identified in the NetCDF file.

    Parameter
    ----------
    fname: str
        The name of the NetCDF file to be converted to CSV file(s)
    """
    xr.set_options(use_new_combine_kwarg_defaults=True)
    num_csv_files = 0
    schemas = {}

    try:
        # Open file as xarray datatree
        data = xr.open_datatree(fname)

        # Loops datatree items to gather info for various dimension groups
        for path,ds in data.to_dict().items():
            if path=="/": 
                path=""
            variables = list(ds.variables)
            products = [f"{path}/{vv}" for vv in variables if vv not in ds.coords]
            for varname in products:
                dims = data[varname].dims
                if dims not in schemas:
                    schemas[dims] = []
                schemas[dims].append(varname)

        input_filename = fname.split('/')[-1]
        vals = list(schemas.values())

        # Create the zip file object in write mode
        with zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
            logger.info(f'Creating {len(vals)} CSV files for {input_filename}')
            for idx in range(len(vals)):
                op_file = f"{input_filename}-{idx}.csv"
                with zf.open(op_file, 'w', force_zip64=True) as csv_file:
                    vvs = vals[idx]
                    ds = xr.combine_by_coords([data[vv].rename(vv) for vv in vvs])

                    # Get primary dimension variable name
                    dim_var = list(ds.sizes.keys())[0]

                    chunk_size = 1000
                    data_len = len(ds[f'{dim_var}'])
                    for i in range(0, data_len, chunk_size):
                        # Process a slice of the dataset
                        indexer = {dim_var: slice(i, i + chunk_size)}
                        ds_chunk = ds.isel(indexer)

                        # Convert the small chunk to a pandas DataFrame
                        df_chunk = ds_chunk.to_dataframe().dropna(how='all', subset=vvs)
                        
                        # Write header for the first chunk only
                        df_chunk.to_csv(csv_file, header=(i==0))

                        del df_chunk
                logger.info(f' {op_file} added to zip file')
                num_csv_files += 1

    except Exception as e:
        logger.error("File conversion failed: %s", e)
        raise

    return num_csv_files

def main():
    """Entry point for the casper command line tool."""
    logging.basicConfig(
        stream=sys.stdout,
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    if len(sys.argv) < 2:
        print(f"Must specify an input file")
        exit()

    input_file = sys.argv[1]
    
    """Parse arguments and run casper on specified input file."""
    if not valid_input_file(input_file):
            raise ValueError("Input filename not valid")

    if not valid_workable_file(input_file):
            raise ValueError("Input file not valid")
    zip_file_name = f"{input_file.split('/')[-1].split('.')[0]}.zip"

    convert_to_csv(input_file, zip_file_name)
    
if __name__ == "__main__":
    main()