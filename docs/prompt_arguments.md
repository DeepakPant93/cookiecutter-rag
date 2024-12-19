### Prompt Arguments

When you run the `cookiecutter` command, you'll be prompted to configure your repository with various input values. Here’s an explanation of each prompt value:

---

#### **author**

Your full name.

#### **email**

Your email address.

#### **author_github_handle**

Your GitHub handle, i.e., `<handle>` in `https://github.com/<handle>`.

#### **project_name**

The name of your project. This should match the repository name and contain only alphanumeric characters and hyphens (`-`).

#### **project_slug**

A slug for your project. By default, this is derived from `project_name` with hyphens (`-`) replaced by underscores (`_`). This is used for importing code, e.g.:

```python
from <project_slug> import foo
```

#### **project_description**

A brief description of your project.

#### **dockerhub_username**

Your Docker Hub username, i.e., `<handle>` in `https://hub.docker.com/u/<handle>`.

#### **include_github_actions**

Set this to `"y"` or `"n"`. If enabled, a `.github` directory will be created with actions and workflows for setting up the environment, running code formatting checks, and executing unit tests.

#### **app_host_port**

The port on which the application will run. Defaults to `80`.

#### **open_source_license**

Select a license for your project. Options include:
`["1. MIT License", "2. BSD license", "3. ISC license", "4. Apache Software License 2.0", "5. GNU General Public License v3", "6. Not open source"]`
