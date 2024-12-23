# Linting and code quality

Code can be linted and quality-checked with the command

```bash
make lint
```

Note that this requires the pre-commit hooks to be installed.

This command will run the following tools:

## ruff

[ruff](https://github.com/charliermarsh/ruff) is used to lint and format the code, and it is configured through `pyproject.toml`:

```
[tool.ruff]
target-version = "py37"
line-length = 120
fix = false
select = [
    # flake8-2020
    "YTT",
    # flake8-bandit
    "S",
    # flake8-bugbear
    "B",
    # flake8-builtins
    "A",
    # flake8-comprehensions
    "C4",
    # flake8-debugger
    "T10",
    # flake8-print
    "T20",
    # flake8-simplify
    "SIM",
    # isort
    "I",
    # mccabe
    "C90",
    # pycodestyle
    "E", "W",
    # pyflakes
    "F",
    # pygrep-hooks
    "PGH",
    # pyupgrade
    "UP",
    # ruff
    "RUF",
    # tryceratops
    "TRY",
]
ignore = [
    # LineTooLong
    "E501",
    # DoNotAssignLambda
    "E731",
]

[tool.ruff.per-file-ignores]
"tests/*" = ["S101"]
```

# Typechecking

`mypy` is used for static type checking.

## mypy

[mypy](https://mypy.readthedocs.io/en/stable/) can be used for static type checking, and its configuration and can be edited in `pyproject.toml`.

```toml
[tool.mypy]
disallow_untyped_defs = "True"
disallow_any_unimported = "True"
no_implicit_optional = "True"
check_untyped_defs = "True"
warn_return_any = "True"
warn_unused_ignores = "True"
show_error_codes = "True"
exclude = [
    '\.venv',
    '{{cookiecutter.project_name}}',
    'tests'
]
```

# deptry

[deptry](https://github.com/fpgmaas/deptry) is used to check the code for dependency issues, and its configuration and can be edited in `pyproject.toml`.

```toml
[tool.mypy]
disallow_untyped_defs = "True"
disallow_any_unimported = "True"
no_implicit_optional = "True"
check_untyped_defs = "True"
warn_return_any = "True"
warn_unused_ignores = "True"
show_error_codes = "True"
exclude = [
    '\.venv',
    '{{cookiecutter.project_name}}',
    'tests'
]
```

# Prettier

[Prettier](https://prettier.io/) is used to format the markdown documentation, along with any json and yaml files.
Its options can be configured in the included `.editorconfig` file or in greater detail by adding a `.prettierrc` file ([See Docs](https://prettier.io/docs/en/configuration)).

```yaml
[*]
max_line_length = 120

[*.json]
indent_style = space
indent_size = 4
```

## Github Actions

The code formatting is checked for every merge request, every merge to main, and every release.
