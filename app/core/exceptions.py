from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI):
    """
    Register global exception handlers for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.

    This function attaches a custom exception handler that will catch any
    unhandled exceptions across the application and return a JSON response
    with status code 500.
    """

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        """
        Handle all uncaught exceptions and return a generic 500 error response.

        Args:
            request (Request): The incoming HTTP request object.
            exc (Exception): The unhandled exception that was raised.

        Returns:
            JSONResponse: A JSON error response with status code 500.
        """
        # Convert the exception message into a JSON response
        return JSONResponse(
            status_code=500,
            content={'detail': str(exc)}  # Include the exception message for debugging
        )
