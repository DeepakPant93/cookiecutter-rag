"""

This module defines custom exception classes and error-handling utilities tailored
to the needs of a data science pipeline. It helps standardize error reporting, improve
debugging, and provide meaningful feedback during model training, data preprocessing,
and prediction processes.

Classes:
    DataValidationError: Raised when input data fails validation checks.
    ModelTrainingError: Raised during errors in the model training phase, such as convergence issues or invalid configurations.
    PredictionError: Raised when the prediction pipeline encounters issues, such as missing features or incompatible input formats.
    PipelineExecutionError: Raised for generic errors occurring during pipeline execution.

Usage:
    Import and use the exceptions in various stages of the data science pipeline:

    Example:
        ```python
        from exception import DataValidationError, ModelTrainingError

        try:
            validate_data(input_data)
        except DataValidationError as e:
            logger.error(f"Data validation failed: {e}")
            raise
        ```

Features:
    - Custom exceptions for specific pipeline stages, ensuring meaningful error reporting.
    - Enables targeted exception handling, reducing debugging time.
    - Provides a consistent structure for error messages across the project.

Purpose:
    - To define project-specific exceptions for common error scenarios in the pipeline.
    - To improve the robustness and reliability of the pipeline by enabling clear error handling.
    - To make the debugging process more intuitive by raising descriptive errors.

Examples:
    - **Data Validation**: Raise a `DataValidationError` if the input data schema is incorrect or missing required fields.
    - **Model Training**: Raise a `ModelTrainingError` if the model fails to converge due to invalid hyperparameters.
    - **Prediction**: Raise a `PredictionError` when incompatible input data is passed to the model.

Additional Notes:
    - Use these exceptions in conjunction with logging to provide detailed error information.
    - Ensure that custom exceptions are raised with meaningful messages to assist in debugging and error resolution.
"""

from fastapi import HTTPException


class CustomException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        """
        Custom exception for handling API errors.

        :param status_code: The HTTP status code to return.
        :param detail: A string describing the error in detail.
        """
        super().__init__(status_code=status_code, detail=detail)
