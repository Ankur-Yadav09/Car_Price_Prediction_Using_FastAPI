from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import create_token

# Create a new router for authentication-related endpoints
router = APIRouter()


class AuthInput(BaseModel):
    """
    Schema for user login input.

    Attributes:
        username (str): The username of the user.
        password (str): The user's password.
    """
    username: str
    password: str


@router.post('/login')
def login(auth: AuthInput):
    """
    Authenticate user and generate a JWT access token.

    Args:
        auth (AuthInput): User login data containing username and password.

    Returns:
        dict: JSON response with an access token if authentication is successful,
              otherwise an error message.
    """
    # Simple hardcoded authentication check (for demo purposes only).
    # In a real-world application, validate against a database.
    if (auth.username == 'admin') and (auth.password == 'admin'):
        token = create_token({'sub': auth.username})
        return {'access_token': token}

    # Return error if credentials are invalid
    return {'error': 'Invalid Credentials'}
