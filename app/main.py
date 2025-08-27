from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

# Initialize FastAPI application
app = FastAPI(title="Car Price Prediction API")

# ----------------------------
# Middleware
# ----------------------------
# Attach custom logging middleware to log requests and responses
app.add_middleware(LoggingMiddleware)

# ----------------------------
# Routes / Endpoints
# ----------------------------
# Authentication routes (login, token handling)
app.include_router(routes_auth.router, tags=["Auth"])

# Prediction routes (car price prediction)
app.include_router(routes_predict.router, tags=["Prediction"])

# ----------------------------
# Monitoring
# ----------------------------
# Integrate Prometheus metrics for monitoring
# Exposes /metrics endpoint automatically
Instrumentator().instrument(app).expose(app)

# ----------------------------
# Exception Handling
# ----------------------------
# Register global exception handlers (e.g., for unhandled errors)
register_exception_handlers(app)
