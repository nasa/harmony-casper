# Scripts

Automation scripts used by CI/CD workflows. Most are called automatically by GitHub Actions.

## verify_tag.sh

Verifies git tags match the version in `pyproject.toml` before publishing to PyPI.

**Called by:** `.github/workflows/publish.yml`
