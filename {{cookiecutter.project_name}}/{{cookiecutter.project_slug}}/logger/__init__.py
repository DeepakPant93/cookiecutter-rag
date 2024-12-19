"""

This module provides centralized logging utilities for the data science pipeline.
It standardizes logging practices, ensures consistency across components, and facilitates
easy debugging and monitoring of the pipeline's execution, including data preprocessing,
model training, evaluation, and predictions.

Functions:
    setup_logging: Configures the logging system, including log format, level, and output destinations.
    get_logger: Returns a logger instance for a specific module or stage of the pipeline.

Features:
    - Centralized logging configuration to maintain consistency.
    - Support for different log levels (INFO, DEBUG, WARNING, ERROR, CRITICAL).
    - Ability to write logs to files, console, or external monitoring systems.
    - Timestamped log entries for accurate tracking of events.
    - Integration with custom exception handling for detailed error reporting.

Usage:
    Use this module to log messages in a standardized manner across the project:

    Example:
        ```python
        from src.logging import logger

        logger.info("Starting the model training process...")
        logger.error("An error occurred during data validation.")
        ```

Purpose:
    - To provide a standardized mechanism for logging messages throughout the data science pipeline.
    - To assist in debugging by capturing detailed logs of each pipeline stage.
    - To enable seamless integration with monitoring and alerting systems.

Best Practices:
    - Use appropriate log levels to categorize messages (e.g., DEBUG for detailed information, ERROR for issues).
    - Ensure logs include sufficient context, such as function names or input details, to aid debugging.
    - Regularly monitor log files for anomalies or errors in the pipeline.

Additional Notes:
    - The `setup_logging` function can be configured to write logs to multiple destinations, such as files or cloud services.
    - The module can be extended to integrate with third-party monitoring tools like Elasticsearch, Splunk, or Datadog.
"""

import logging
import os
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"{{cookiecutter.project_name}}.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("{{cookiecutter.project_name}}-logger")
