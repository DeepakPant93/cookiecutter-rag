# Builder Stage
FROM python:3.12-slim AS builder

# Set environment variables for Poetry
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    PATH="/opt/poetry/bin:$PATH"

# Install Poetry and necessary tools
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get remove -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy only the dependency files first to leverage Docker caching
COPY pyproject.toml poetry.lock /app/

# Install dependencies (only for building the wheel)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# Copy the rest of the application code
COPY . /app

# Build the wheel file
RUN poetry build -f wheel

# Runtime Stage
FROM python:3.12-slim AS runtime

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the built wheel file from the builder stage
COPY --from=builder /app/dist/*.whl /app/

# Install the wheel file
RUN pip install --no-cache-dir /app/*.whl

# Expose application port
EXPOSE {{cookiecutter.app_host_port}}

# Command to run the application
CMD ["{{cookiecutter.project_slug}}"]
