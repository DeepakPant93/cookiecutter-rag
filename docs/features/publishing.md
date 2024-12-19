# Publishing to PyPI or Artifactory

## Releasing from GitHub

To successfully publish your project from the release workflow, you'll need to add some secrets to your GitHub repository so they can be used as environment variables.

### Set-up for PyPI

To publish to PyPI, you'll need to set the secret `PYPI_TOKEN` in your repository. Here's how to do it:

1. Navigate to `Settings > Secrets > Actions` in your GitHub repository and click `New repository secret`.
2. Name the secret `PYPI_TOKEN`.
3. In a new tab, go to your [PyPI Account settings](https://pypi.org/manage/account/) and select `Add API token`.
4. Copy the token and paste it into the `Value` field for the GitHub secret you created in the previous step. You're all set!

## Publishing from Your Local Machine

While it is possible to release locally, it is not recommended. If you choose to release locally, set the repository secrets as environment variables on your local machine and run:

```bash
make bake-and-publish
```
