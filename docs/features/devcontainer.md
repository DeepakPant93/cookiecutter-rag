# Reproducible Development Environments with VSCode DevContainers

This project includes a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) configuration located in the `.devcontainer` directory. The devcontainer utilizes the VSCode [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) specification to create a consistent and reproducible development environment.

It pre-installs all dependencies, including those required by Poetry, for project development, testing, and building. Additionally, the devcontainer sets up pre-commit hooks and configures the VSCode Python extension to use the correct Python interpreter and pytest paths.
