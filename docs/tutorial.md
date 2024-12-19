# Tutorial: Setting Up Your Project

This guide will walk you through setting up a Python project using the **cookiecutter-rag** template, ideal for Generative AI RAG application development. Follow these steps to get started!

## Step 1: Install Poetry

To begin, you need to install **Poetry** for dependency management. You can find the installation instructions on the [Poetry website](https://python-poetry.org/docs/).

After installing Poetry, it's recommended to configure it to create virtual environments within the project directory:

```bash
poetry config virtualenvs.in-project true
```

This will ensure that new virtual environments are created inside the `./.venv` directory by default whenever you run `poetry init`.

## Step 2: Install pyenv (Optional)

While this step is optional, **pyenv** is a useful tool for managing multiple Python versions. If you prefer another method for managing Python versions, feel free to skip this step.

To install pyenv, follow the instructions on the [pyenv GitHub page](https://github.com/pyenv/pyenv).

To install a specific Python version with pyenv, run:

```bash
pyenv install --list  # to see available versions
pyenv install -v 3.9.7  # replace 3.9.7 with the version you want
```

## Step 3: Generate Your Project

First, navigate to the directory where you want your project to be created. Then, install the **cookiecutter-rag** package with the following command:

```bash
pip install cookiecutter-rag
```

For more information about the prompt arguments, refer to the [Prompt Arguments](./prompt_arguments.md) section.

Alternatively, you can install **cookiecutter** and pass the GitHub repository URL directly:

```bash
pip install cookiecutter
cookiecutter git@github.com:DeepakPant93/cookiecutter-rag.git
```

## Step 4: Set Up Your GitHub Repository

Create a new empty repository on GitHub. You can do this by visiting [GitHub's new repository page](https://github.com/new). Make sure the repository name only contains alphanumeric characters and optionally a hyphen (`-`). **Do not** check any boxes under "Initialize this repository with".

## Step 5: Upload Your Project to GitHub

Once your project is ready, run the following commands to upload it to GitHub. Replace `<project-name>` with the name of your repository, and `<github_author_handle>` with your GitHub username:

```bash
cd <project_name>
git init -b main
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

## Step 6: Activate Your Environment

If you're using **pyenv**, set the Python version for your project:

```bash
pyenv local x.y.z  # Replace x.y.z with the Python version you want to use
```

Next, install and activate the Poetry environment by running:

```bash
make bake-env
poetry shell
```

## Step 7: Sign Up for Codecov

If you’ve enabled code coverage in your project, sign up for [Codecov](https://about.codecov.io/language/python/) using your GitHub account.

## Step 8: Configure Your Repository Secrets

To enable deployment to **PyPI** via GitHub Actions, you’ll need to configure repository secrets. For detailed instructions, see [Setting up for PyPI](./features/publishing.md#set-up-for-pypi).

## Step 9: Create a New Release

To trigger a release, go to the **Releases** tab in your GitHub repository. Click **Draft a new release**. If you can't find the button, go directly to the URL: `https://github.com/<username>/<repository-name>/releases/new`.

Create a new tag in the format `*.*.*`, where `*` represents alphanumeric characters. Finally, click **Publish release** to trigger the release.

## Step 10: Enable Documentation

To enable documentation with **MkDocs** on GitHub Pages, navigate to your repository's **Settings** > **Code and Automation** > **Pages**. Once the release is published, you should see a notification saying, _Your site is ready to be published at https://<author_github_handle>.github.io/<project_name>/_.

Under **Source**, select the `gh-pages` branch.

## Step 11: You're All Set!

Congratulations! Your project is now set up and ready for development. The CI/CD pipeline will run automatically when you open a pull request, merge to the `main` branch, or create a new release.

If you have any suggestions for improvements, feel free to [open an issue](https://github.com/<username>/<repository-name>/issues) or submit a pull request!
