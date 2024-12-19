# Cookiecutter General AI RAG Application Development Template

This is a modern **Cookiecutter** template for initializing Python projects, particularly for **General AI RAG Application Development**. It provides a comprehensive setup for development, testing, and deployment, incorporating essential tools for effective project management.

## Features

This template includes the following features:

-   **[Poetry](https://python-poetry.org/)** for dependency management
-   **CI/CD** with **[GitHub Actions](https://github.com/features/actions)**
-   **Pre-commit hooks** using **[pre-commit](https://pre-commit.com/)**
-   **Code quality checks** with **[ruff](https://github.com/charliermarsh/ruff)**, **[mypy](https://mypy.readthedocs.io/en/stable/)**, **[deptry](https://github.com/fpgmaas/deptry/)**, and **[prettier](https://prettier.io/)**
-   **Publishing to [PyPI](https://pypi.org)** via GitHub releases
-   **Testing and coverage** with **[pytest](https://docs.pytest.org/en/7.1.x/)** and **[codecov](https://about.codecov.io/)**
-   **Documentation generation** with **[MkDocs](https://www.mkdocs.org/)**
-   **Python compatibility testing** with **[Tox](https://tox.wiki/en/latest/)**
-   **Containerization** using **[Docker](https://www.docker.com/)**
-   **Development environment** with **[VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)**
-   **Deployment** with **[Azure Container Apps](https://azure.microsoft.com/en-in/products/container-apps)**

You can find an example repository created using this template [here](https://github.com/DeepakPant93/cookiecutter-rag).

## Quickstart

To get started, follow these steps:

### Step 1: Install `cookiecutter-rag`

First, navigate to the directory where you want to create the project and run:

```bash
pip install cookiecutter-rag
```

Alternatively, you can install **cookiecutter** and use the GitHub repository URL directly:

```bash
pip install cookiecutter
cookiecutter git@github.com:DeepakPant93/cookiecutter-rag.git
```

### Step 2: Create a GitHub Repository

Create a new repository on GitHub, then run the following commands in your terminal, replacing `<project-name>` with your GitHub repository name and `<github_author_handle>` with your GitHub username:

```bash
cd <project_name>
make init-repo
```

### Step 3: Install the Environment and Pre-commit Hooks

Run the following command to install the environment and pre-commit hooks:

```bash
make bake-env
```

Now you're all set to start development! The CI/CD pipeline will automatically trigger on pull requests, merges to the main branch, and new releases.

For instructions on publishing to **PyPI**, refer to [this guide](./features/publishing.md#set-up-for-pypi). To enable automatic documentation with **MkDocs**, follow the steps in [this guide](./features/mkdocs.md). For code coverage setup, refer to [this guide](./features/codecov.md).

## Documentation

You can find the documentation for this template [here](https://DeepakPant93.github.io/cookiecutter-rag/).

## Acknowledgements

This project is inspired by **[Audrey Feldroy's](https://github.com/audreyfeldroy)** excellent work on the [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) template.
