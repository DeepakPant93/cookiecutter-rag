# Dependency Management with Poetry

The generated repository uses [Poetry](https://python-poetry.org/) for dependency management. Once you've created your repository using this cookiecutter template, a Poetry environment is pre-configured in the `pyproject.toml` and `poetry.toml` files. To add project-specific dependencies, run:

```bash
poetry add <package>
```

Then, install the environment by running:

```bash
make bake-env
```

By default, the environment is created in a `.venv` folder. You can easily start an interactive shell within the environment using:

```bash
poetry shell
```
