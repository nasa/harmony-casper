

# Overview

**CASPER** – CSV Automation Service for Processing & Easy Retrieval

CASPER is a Python package that converts NetCDF (.nc, .h5) files to one or more CSV files based on the dimensional schema in the NetCDF file.

### What does it do?

Using xarray, CASPER obtains the dimensions identified in the NetCDF file and groups variables by the dimensional schema, then outputs each dimensional schema in a separate CSV file.

# Getting started, with poetry

1. Follow the instructions for installing `poetry` [here](https://python-poetry.org/docs/).
2. Install `casper`, with its dependencies, by running the following from the repository directory:

```shell
poetry install
```

## Usage

For example:

```shell
poetry run casper TEMPO_NO2_L2_V04_S009G07.nc 
```
For example (_note that these are pseudo-real, not actual, TEMPO file names_):

```shell
casper TEMPO_NO2_L2_V04_S009G07.nc
```

**Output:**
- `Zip file TEMPO_NO2_L2_V04_S009G07.zip including csv files
-   `TEMPO_NO2_L2_V04_S009G07-0.csv`, → dimension 1 (ie, dimensions ('mirror_step', 'xtrack', 'corner'))
-   `TEMPO_NO2_L2_V04_S009G07-1.csv`, → dimension 2 (ie, dimensions('mirror_step', 'xtrack', 'swt_level'))


### Key Features
- Reads NetCDF files and groups the data by shared dimensions and creates a CSV file for each dimension group.
- Command-line interface and Python API for integration with NASA Harmony service orchestrator
- Verbose logging for debugging

## Installation

### From PyPI (Recommended)
```shell
pip install casper
```

### From Source (Development)

For local development or the latest features:

```shell
git clone <Repository URL>
cd casper
```

**(Option A) using poetry (Recommended for development):**

```shell
# Install poetry: https://python-poetry.org/docs/
poetry install
```

**(Option B) using pip:**

```shell
pip install .
```

## Usage

### Basic Usage

```shell
casper file_name
```

### With Poetry (if installed via poetry)
```shell
poetry run casper filename
```


## Contributing

Issues and pull requests welcome on [GitHub](https://github.com/nasa/harmony-casper/).

## License & Attribution

CASPER is released under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).

