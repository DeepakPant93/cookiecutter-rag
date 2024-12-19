# Containerization with Docker

This project includes a `Dockerfile` in the root directory, which installs Poetry, sets up the environment, and runs `main.py` when executed.

To build the Docker image, use the following command:

```bash
docker build . -t my-docker-image
```

Once the image is built, it can be run in the background using:

```bash
docker run -d my-docker-image
```

Alternatively, to run the container in interactive mode, use:

```bash
docker run --rm -it --entrypoint bash my-docker-image
```
