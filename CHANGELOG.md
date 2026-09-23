# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Common Changelog](https://common-changelog.org/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Changed
- Renamed project to `harmony-casper` to avoid name collision in PyPI. ([#47](https://github.com/nasa/harmony-casper/pull/47))

## [1.0.0] - 2026-09-22

### Added
- Added a GitHub Actions workflow to build and publish releases to PyPI. ([#11](https://github.com/nasa/harmony-casper/issues/11))

- Updated the order of output csv filenames Ensure that the dimensional schemas are processed in a deterministic order. ([#16](https://github.com/nasa/harmony-casper/issues/16))

### Changed
- Implemented new streamlined release workflow. ([#28](https://github.com/nasa/harmony-casper/issues/28))

## [0.2.0] - 2026-03-10

### Changed

- Switched dependency management and packaging from Poetry to uv for faster installs and simplified workflow. ([#12](https://github.com/nasa/harmony-casper/issues/12))
