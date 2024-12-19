# Makefile

The generated repository will have a `Makefile` available. A list of all
available commands that are available can be obtained by running
`make help` in the terminal. Initially, if all features are selected, the following commands are
available:

```
help                      Display this help message
bake-env                  Install the poetry environment and set up pre-commit hooks
clean-env                 Remove the poetry environment
reset-env                 Install the poetry environment and set up pre-commit hooks
init-repo                 Initialize git repository
setup-cloud-env           Create resource group, container app environment, and service principal
clean-cloud-env           Delete resource group, container app environment, and service principal
bake-dvc                  Initialize DVC and set up service account
clean-dvc                 Clean up DVC and service account
lint                      Run code quality tools
test                      Run tests with pytest
bake                      Build wheel file using poetry
clean-bake                Clean build artifacts
publish                   Publish a release to PyPI
bake-and-publish          Build and publish to PyPI
update                    Update project dependencies
run                       Run the project's main application
docs-test                 Test if documentation can be built without warnings or errors
docs                      Build and serve the documentation
bake-container            Build Docker image
container-push            Push Docker image to Docker Hub
bake-container-and-push   Build and push Docker image to Docker Hub
clean-container           Clean up Docker resources related to the app
dvc-add-data              Add a data file to DVC and Git, and enable autostage in DVC
dvc-push-data             Push changes to Git
dvc-pull-data             Push changes to Git
dvc-run-pipeline          Run DVC pipeline
print-dependency-tree     Initialize DVC and set up service account
teardown                  Clean up temporary files and directories and destroy the virtual environment, Docker image from your local machine
teardown-all              Clean up temporary files and directories and destroy the virtual environment, Docker image, and Cloud resources
```
