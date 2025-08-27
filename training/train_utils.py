import os

# ----------------------------
# Data file configuration
# ----------------------------

# Directory where raw data is stored
DATA_DIR = 'data'

# Name of the dataset file
DATA_FILE_NAME = 'car-details.csv'

# Full path to the dataset file
DATA_FILE_PATH = os.path.join(DATA_DIR, DATA_FILE_NAME)


# ----------------------------
# Model file configuration
# ----------------------------

# Application base directory
APP_DIR = 'app'

# Sub-directory where trained ML models are stored
MODEL_DIR_NAME = 'models'

# Filename of the saved ML model
MODEL_NAME = 'model.joblib'

# Full path to the model directory
MODEL_DIR = os.path.join(APP_DIR, MODEL_DIR_NAME)

# Full path to the saved ML model file
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)
