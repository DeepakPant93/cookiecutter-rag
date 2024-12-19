# Unit Testing with Pytest

[Pytest](https://docs.pytest.org/en/7.1.x/) is automatically included in the environment. A template unit test is created in the `tests` directory when the project is set up. You can run the tests using:

```bash
make test
```

If `include_github_actions` is set to `"y"`, the tests will automatically run for every merge request, merge to the main branch, and release.
