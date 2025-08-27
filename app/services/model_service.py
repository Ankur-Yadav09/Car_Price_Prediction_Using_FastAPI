import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import set_cached_prediction, get_cached_prediction

# Load the trained ML model pipeline (includes preprocessing + regressor)
model = joblib.load(settings.MODEL_PATH)


def predict_car_price(data: dict) -> float:
    """
    Predict the selling price of a car given its features.
    Uses Redis caching to avoid redundant model predictions.

    Args:
        data (dict): A dictionary of input features for prediction.

    Returns:
        float: The predicted car price.
    """
    # Create a unique cache key from input values (simple concatenation)
    cache_key = " ".join([str(val) for val in data.values()])

    # Check if prediction already exists in cache
    cached = get_cached_prediction(cache_key)
    if cached:
        return cached

    # Convert input dictionary into a DataFrame for model inference
    input_data = pd.DataFrame([data])

    # Run model prediction
    prediction = model.predict(input_data)[0]

    # Store prediction result in cache
    set_cached_prediction(cache_key, prediction)

    return prediction
