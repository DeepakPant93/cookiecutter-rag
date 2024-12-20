from fastapi import FastAPI, responses
from fastapi.openapi.utils import get_openapi
from fastapi_health import health

from {{cookiecutter.project_slug}}.api.endpoint import router

__version__ = "0.0.1"

app = FastAPI(
    title="{{cookiecutter.project_name}} APIs",
    description="{{cookiecutter.project_description}}",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
)


app = FastAPI()

@app.get("/", include_in_schema=False)
async def root() -> responses.RedirectResponse:
    """
    Redirects the root URL to the API documentation page.

    Returns:
        RedirectResponse: A response object that redirects the client to the "/docs" URL.
    """

    return responses.RedirectResponse("/docs")


# Health Check
async def health_check() -> dict:
    """
    Checks the health of the API.

    This endpoint checks the health of the API and returns a simple status
    message. It is intended to be used by load balancers or other monitoring
    systems to determine if the API is functional.

    Returns:
        dict: A dictionary containing the status of the API.
    """
    return {"status": "healthy"}


# Include routers
app.add_api_route(
    "/health",
    health([health_check]),
    tags=["Management"],
    description="Management APIs",
)
app.include_router(router, prefix="/api/v1", tags=["Operations"])


def _custom_openapi() -> dict:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="{{cookiecutter.project_name}} APIs",
        description="{{cookiecutter.project_description}}",
        version=__version__,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = _custom_openapi


def main() -> None:
    """
    The main entry point of the application.

    This function starts the FastAPI server using Uvicorn. It serves the API
    on the specified host and port. The function is intended to be run
    directly when the script is executed.

    Notes:
        - The 'nosec B104' comment is used to suppress a security warning
          related to binding to all network interfaces.
    """

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port={{cookiecutter.app_host_port}})  # nosec B104


if __name__ == "__main__":
    main()
