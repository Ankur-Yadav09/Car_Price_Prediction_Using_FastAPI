import logging
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Custom middleware for logging HTTP requests and responses.

    Logs the HTTP method, request URL, and response status code
    for every incoming request to the FastAPI/Starlette application.
    """

    async def dispatch(self, request, call_next):
        """
        Process each request/response cycle.

        Args:
            request (Request): The incoming HTTP request object.
            call_next (Callable): Function that passes the request
                                  to the next middleware or endpoint.

        Returns:
            Response: The HTTP response returned by the application.
        """
        # Log request details
        logging.info(f"Request: {request.method} {request.url}")

        # Continue processing the request and get the response
        response = await call_next(request)

        # Log response status code
        logging.info(f"Response: {response.status_code}")

        return response
