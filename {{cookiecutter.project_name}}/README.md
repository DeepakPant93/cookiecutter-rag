# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>
- **Documentation** <https://{{cookiecutter.author_github_handle}}.github.io/{{cookiecutter.project_name}}/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

## Installation

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

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.
