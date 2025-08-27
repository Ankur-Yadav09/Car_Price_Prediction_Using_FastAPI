import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the system environment.
# This allows sensitive data (like API keys, secrets, DB URLs) to be stored securely
load_dotenv()


class Settings:
    """
    Central configuration class for the Car Price API.

    This class stores all the important application-level settings,
    such as API keys, JWT secrets, Redis connection, and model path.
    Values are loaded from environment variables when available,
    otherwise sensible defaults are used.

    Attributes:
        PROJECT_NAME (str): Name of the project/application.
        API_KEY (str): API key for authenticating requests.
        JWT_SECRET_KEY (str): Secret key for signing JWT tokens.
        JWT_ALGORITHM (str): Algorithm used for JWT signing and validation.
        REDIS_URL (str): URL for the Redis server used as cache/store.
        MODEL_PATH (str): File path to the machine learning model.
    """

    # Application name
    PROJECT_NAME = 'Car Price API'

    # API key (default: demo-key if not found in .env)
    API_KEY = os.getenv('API_KEY', 'demo-key')

    # JWT token configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret')
    JWT_ALGORITHM = 'HS256'

    # Redis connection string (default: local Redis)
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

    # Path to the ML model file
    MODEL_PATH = 'app/models/model.joblib'


# Create a single instance of settings to be used across the application
settings = Settings()
