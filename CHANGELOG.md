# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Common Changelog](https://common-changelog.org/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Fixed

- Convert scalar NetCDF variables into a one-row CSV schema instead of raising
  `StopIteration`, while preserving chunked conversion for dimensional variables
  ([#41](https://github.com/nasa/harmony-casper/issues/41)).

### Changed

- Implemented new streamlined release workflow. ([#28](https://github.com/nasa/harmony-casper/issues/28))

## [0.2.0] - 2026-03-10

### Changed

- Switched dependency management and packaging from Poetry to uv for faster installs and simplified workflow. ([#12](https://github.com/nasa/harmony-casper/issues/12))
