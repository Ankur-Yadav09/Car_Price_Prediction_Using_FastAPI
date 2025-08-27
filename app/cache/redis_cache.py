import os
import redis
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Redis connection URL from environment
REDIS_URL = os.getenv("REDIS_URL")

# Initialize Redis client (decode_responses=True makes values return as strings instead of bytes)
redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)


def get_cached_prediction(key: str):
    """
    Retrieve a cached prediction from Redis.

    Args:
        key (str): The cache key for the stored prediction.

    Returns:
        dict | None: The cached prediction as a dictionary if found, otherwise None.
    """
    # Fetch value from Redis
    value = redis_client.get(key)
    # Convert string back into dictionary 
    return eval(value) if value else None


def set_cached_prediction(key: str, value: dict):
    """
    Store a prediction result in Redis cache.

    Args:
        key (str): The cache key under which the prediction is stored.
        value (dict): The prediction result to cache.
    """
    # Convert dictionary to string and store in Redis
    redis_client.set(key, str(value))
