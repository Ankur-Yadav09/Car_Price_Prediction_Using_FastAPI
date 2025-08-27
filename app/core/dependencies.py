from fastapi import Header, HTTPException
from app.core.config import settings
from app.core.security import verify_token


def get_api_key(api_key: str = Header(...)) -> str:
    """
    Dependency function to validate the provided API key.

    Args:
        api_key (str): API key passed in the request header.

    Raises:
        HTTPException: If the API key is invalid.

    Returns:
        str: The valid API key.
    """
    # Check if provided API key matches the expected one from settings
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail='Invalid API Key')
    return api_key


def get_current_user(token: str = Header(...)) -> dict:
    """
    Dependency function to validate and decode the JWT token.

    Args:
        token (str): JWT token passed in the request header.

    Raises:
        HTTPException: If the token is missing, expired, or invalid.

    Returns:
        dict: The decoded JWT payload (user info).
    """
    # Verify token validity
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Invalid JWT Token')
    return payload
