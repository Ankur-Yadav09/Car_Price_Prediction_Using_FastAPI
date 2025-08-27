import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from training.train_utils import DATA_FILE_PATH, MODEL_DIR, MODEL_PATH


# ----------------------------
# Load and preprocess dataset
# ----------------------------

# Load dataset from CSV, remove duplicate rows, and drop unnecessary columns
df = (
    pd.read_csv(DATA_FILE_PATH)
      .drop_duplicates()
      .drop(columns=['name', 'model', 'edition'])  # irrelevant features
)

# Define target variable and feature set
X = df.drop(columns='selling_price')
y = df.selling_price.copy()

# Split dataset into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ----------------------------
# Define preprocessing pipelines
# ----------------------------

# Identify numeric and categorical columns
num_cols = X_train.select_dtypes(include='number').columns.tolist()
cat_cols = [col for col in X_train.columns if col not in num_cols]

# Pipeline for numeric features: impute missing values with median, then scale
num_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Pipeline for categorical features: impute missing with "missing", then one-hot encode
cat_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Combine numeric and categorical transformers into a single preprocessor
preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipe, num_cols),
    ('cat', cat_pipe, cat_cols)
])


# ----------------------------
# Define and train model
# ----------------------------

# Random Forest Regressor with limited trees & depth (to prevent overfitting)
regressor = RandomForestRegressor(
    n_estimators=10, max_depth=5, random_state=42
)

# Build full pipeline: preprocessing + model
rf_model = Pipeline(steps=[
    ('pre', preprocessor),
    ('reg', regressor)
])

# Train the model on training data
rf_model.fit(X_train, y_train)


# ----------------------------
# Save trained model
# ----------------------------

# Ensure model directory exists, then save trained pipeline as .joblib
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(rf_model, MODEL_PATH)
