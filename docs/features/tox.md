# Compatibility Testing with Tox

This project uses [Tox](https://tox.wiki/en/latest/) to test compatibility across multiple Python versions. By default, the project is tested with Python versions `3.10`, `3.11`, and `3.12`. The tests are automatically run in the CI/CD pipeline on every pull request, merge to the main branch, and release.

To add more Python versions, simply update the `tox.ini` file and modify the relevant workflows in the `.github` directory.
