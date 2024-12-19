### Test Coverage with Codecov

Executing `make test` runs the test suite and generates a coverage report in the form of `coverage.xml`. Integration with [Codecov](https://about.codecov.io/) has been added to the CI/CD pipeline for comprehensive test coverage analysis.

To enable Codecov:

1. Sign up at [Codecov.io](https://about.codecov.io/) using your GitHub account.
2. Include a `codecov.yaml` configuration file in your repository with the following default settings:
3. Generate a new token at [Codecov.io](https://about.codecov.io/) and add it to the github secret as `CODECOV_TOKEN`.

```yaml
# Badge color changes from red to green between 70% and 100%
# PR pipeline fails if codecov falls with 1%

coverage:
    range: 70..100
    round: down
    precision: 1
    status:
        project:
            default:
                target: auto
                threshold: 1%
```
