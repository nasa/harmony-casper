# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Common Changelog](https://common-changelog.org/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Changed

- Implemented new streamlined release workflow. ([#28](https://github.com/nasa/harmony-casper/issues/28))

### Fixed

- CSV output is now byte-reproducible across host platforms. `pandas.DataFrame.to_csv` defaults its line terminator to `os.linesep`, so the same granule produced `\r\n` on Windows and `\n` on Linux. ([#38](https://github.com/nasa/harmony-casper/issues/38))
- Output zip names are derived with `Path.stem`, so filenames containing more than one dot are no longer truncated and Windows path separators are handled. ([#38](https://github.com/nasa/harmony-casper/issues/38))
- `casper` invoked without an input file now exits with a message instead of raising `IndexError`. ([#38](https://github.com/nasa/harmony-casper/issues/38))
- Added `.gitattributes` so the byte-compared test fixtures are never line-ending translated on checkout. ([#38](https://github.com/nasa/harmony-casper/issues/38))

## [0.2.0] - 2026-03-10

### Changed

- Switched dependency management and packaging from Poetry to uv for faster installs and simplified workflow. ([#12](https://github.com/nasa/harmony-casper/issues/12))
