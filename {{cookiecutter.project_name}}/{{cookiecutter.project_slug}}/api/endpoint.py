from fastapi import APIRouter

router = APIRouter()


@router.post("/upload-docs")
async def upload_docs() -> dict:
    """
    Endpoint to upload documentation. This function encapsulates
    the logic to upload the documentation and returns a success
    message upon completion.

    Returns:
        dict: A dictionary containing a success message.
    """

    return {"message": "Training Model Successful"}


@router.post("/ask")
async def ask() -> dict:
    """
    Endpoint to handle prediction requests. This function processes
    incoming requests for predictions and returns a success message
    upon completion.

    Returns:
        dict: A dictionary containing a success message.
    """

    return {"message": "Prediction Successful"}
