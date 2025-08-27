from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from app.core.config import settings


def create_token(data: dict, expire_minutes: int = 30) -> str:
    """
    Create a JSON Web Token (JWT) with an expiration time.

    Args:
        data (dict): The payload data to encode into the token.
        expire_minutes (int, optional): Expiration time in minutes. Defaults to 30.

    Returns:
        str: Encoded JWT as a string.
    """
    # Copy the input data so we don't modify the original dictionary
    to_encode = data.copy()

    # Set expiration time (UTC-based)
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    to_encode.update({'exp': expire})

    # Encode the payload using the secret key and algorithm from settings
    return jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


def verify_token(token: str) -> dict | None:
    """
    Verify and decode a JWT token.

    Args:
        token (str): The JWT string to verify.

    Returns:
        dict | None: Decoded payload if valid, otherwise None.
    """
    try:
        # Decode the token using the same secret and algorithm
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError:
        # Return None if token is invalid or expired
        return None
