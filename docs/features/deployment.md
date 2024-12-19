## Deployment with Azure Container App

To deploy your application to Azure Container Apps, follow these steps:

### Step 1: Add `DOCKERHUB_PUSH_TOKEN` to GitHub Secrets

To push the image to **Docker Hub** in the CI/CD pipeline, add the `DOCKERHUB_PUSH_TOKEN` as a GitHub secret. This token allows GitHub Actions to authenticate with Docker Hub for pushing the Docker image.

### Step 2: Add `AZURE_CREDENTIALS` to GitHub Secrets

In order to log in to Azure and deploy the container app, you need to provide Azure credentials. Add `AZURE_CREDENTIALS` to your GitHub secrets. This credential will allow the CI/CD pipeline to authenticate and interact with Azure resources.

You can obtain the necessary Azure credentials by setting up the **Azure CLI** and following the instructions provided by Microsoft:

-   Install the **Azure CLI** from [this link](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

Once the Azure CLI is installed and configured, you can generate the Azure credentials JSON file for GitHub secrets.

### Step 3: Generate Azure Credentials

Run the following command to set up the Azure Container App and create the **Service Principal**:

```bash
make setup-cloud-env
```

This will generate an output JSON, which contains the Azure credentials required for deployment. The JSON will look like this:

```json
{
    "clientId": "<clientId>",
    "clientSecret": "<ClientSecret>",
    "subscriptionId": "<subscriptionId>",
    "tenantId": "<tenentId>",
    "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
    "resourceManagerEndpointUrl": "https://management.azure.com/",
    "activeDirectoryGraphResourceId": "https://graph.windows.net/",
    "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
    "galleryEndpointUrl": "https://gallery.azure.com/",
    "managementEndpointUrl": "https://management.core.windows.net/"
}
```

### Step 4: Add Azure Credentials to GitHub Secrets

Once you have the JSON, add it to GitHub as the secret `AZURE_CREDENTIALS`:

1. Go to your GitHub repository.
2. Navigate to **Settings** > **Secrets** > **New repository secret**.
3. Name the secret `AZURE_CREDENTIALS` and paste the entire JSON content into the value field.

### Step 5: Deploy the Container App

After the credentials are set up, the application will automatically be deployed to Azure after each release. This is handled by the CI/CD pipeline in GitHub Actions.

During the container app setup, the `make setup-cloud-env` command will also provide you with a URL for your deployed app. You can use this URL to access the live application once deployed.

---

### Further Reading

You can explore more about Azure Container Apps in the official documentation here:
[Azure Container Apps Documentation](https://learn.microsoft.com/en-us/azure/container-apps/github-actions).
