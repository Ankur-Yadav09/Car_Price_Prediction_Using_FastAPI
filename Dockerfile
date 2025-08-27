# Use official Python 3.10 base image
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
#  - Upgrade pip
#  - Install required packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Run the FastAPI app with uvicorn when container starts
#  - Host set to 0.0.0.0 (so it's accessible externally)
#  - Port 8000 (default for FastAPI)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
