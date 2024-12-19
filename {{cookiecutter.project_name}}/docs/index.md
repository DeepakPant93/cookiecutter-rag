# {{cookiecutter.project_name}}

[![Release](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/v/release/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/test-check-build.yml?branch=main)](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/test-check-build.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/commit-activity/m/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})
[![License](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})](https://img.shields.io/github/license/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}})

{{cookiecutter.project_description}}
This repository contains a sample Data Science application built with FastAPI, designed to streamline model training and prediction processes via RESTful APIs. The application leverages **Poetry** for dependency management, ensuring a robust and scalable development environment.

---

## Features

### FastAPI Endpoints:

-   `/upload-docs`: API endpoint to upload documents for creating embeddings.
-   `/ask`: API endpoint for querying the system and receiving context-aware answers.

### Poetry for Dependency Management:

-   Simplifies package installation and management.
-   Ensures compatibility and reproducibility of the project environment.

### Scalable Architecture:

-   Modular design with clear separation of concerns.
-   Easy integration of new features or pipelines.

---

## Prerequisites

-   Python >= 3.12
-   Poetry installed (`pip install poetry`)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.
    cd {{cookiecutter.project_name}}
    ```
1. Initialize the repository if it's your first time:

    ```bash
    cd {{cookiecutter.project_name}}
    make init-repo
    ```

2. Install dependencies using Poetry:

    ```bash
    make bake-env
    ```

3. Run the FastAPI server:

    ```bash
    make run
    ```

---

## Project Structure

```plaintext
──{{cookiecutter.project_name}}/
    ├── api         # API route definitions
    ├── config      # Configuration files and settings
    ├── constants   # Static constants and enumerations
    ├── core        # Core logic for the application
    ├── entity      # Definitions of data models and schemas
    ├── exception   # Custom exception classes for error handling
    ├── logger      # Logging setup for the application
    ├── models      # Request and response models
    ├── services    # Business logic and service layer
    ├── utils       # Utility functions (e.g., file handling, data encoding)
    └── main.py     # Entry point for the FastAPI application
```

---

Enjoy building with this RAG FastAPI application! 🚀
