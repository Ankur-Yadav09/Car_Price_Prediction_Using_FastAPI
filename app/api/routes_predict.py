from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key, get_current_user
from app.services.model_service import predict_car_price

# Create a router for prediction-related endpoints
router = APIRouter()


class CarFeatures(BaseModel):
    """
    Schema for car feature input used for price prediction.

    Attributes:
        company (str): Car manufacturer (e.g., "Toyota").
        year (int): Year of manufacture.
        owner (str): Ownership status (e.g., "First Owner").
        fuel (str): Fuel type (e.g., "Petrol", "Diesel").
        seller_type (str): Type of seller (e.g., "Dealer", "Individual").
        transmission (str): Transmission type (e.g., "Manual", "Automatic").
        km_driven (float): Total kilometers driven.
        mileage_mpg (float): Mileage of the car in miles per gallon.
        engine_cc (float): Engine capacity in cubic centimeters.
        max_power_bhp (float): Maximum power in brake horsepower.
        torque_nm (float): Torque in Newton meters.
        seats (float): Number of seats in the car.
    """
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float


@router.post('/predict')
def predict_price(
    car: CarFeatures,
    user=Depends(get_current_user),   # Validate user with JWT token
    _=Depends(get_api_key)            # Validate API key
):
    """
    Predict the selling price of a car based on input features.

    Args:
        car (CarFeatures): Input features for the car.
        user (dict): Decoded JWT payload (injected via dependency).
        _ (str): API key validation (not directly used).

    Returns:
        dict: JSON response containing the predicted car price.
    """
    # Convert Pydantic model to dictionary and make prediction
    prediction = predict_car_price(car.model_dump())

    # Format prediction with commas and 2 decimal places
    return {'predicted_price': f'{prediction:,.2f}'}
