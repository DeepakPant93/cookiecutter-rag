# Documentation with MkDocs

Project documentation is automatically generated using [MkDocs](https://www.mkdocs.org/). If `"include_github_actions"` is set to `"y"`, the documentation is automatically deployed to the `gh-pages` branch and is accessible at `https://<github_handle>.github.io/<project_name>/`.

To view the documentation locally, run the following command:

```bash
make docs
```

This will generate and build the documentation, and start a local server, making it accessible at [http://localhost:8000](http://localhost:8000).

## Enabling Documentation on GitHub

To enable documentation on GitHub:

1. Go to `Settings > Actions > General`, and under `Workflow permissions`, select `Read and write permissions`.
2. Create a new release for your project.
3. Navigate to `Settings > Code and Automation > Pages`. If the release was successfully created, you should see a notification saying `Your site is ready to be published at https://<author_github_handle>.github.io/<project_name>/`.
4. Under `Source`, select the `gh-pages` branch. Your documentation should go live within a few minutes.

## Documenting Docstrings

The project automatically converts all docstrings into readable documentation. By default, the project is configured to use [Google style](https://google.github.io/styleguide/pyguide.html) docstrings.

Here is an example of a Google-style docstring:

```python
def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Example function with PEP 484 type annotations.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.
    """
```

For more examples, refer to the [Napoleon documentation](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
