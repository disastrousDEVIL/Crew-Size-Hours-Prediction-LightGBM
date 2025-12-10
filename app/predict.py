import joblib
import pandas as pd
from pathlib import Path
from utils.features import add_engineered_features

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

# Load both models once at startup
model_hours = joblib.load(MODELS_DIR / "model_hours.pkl")
model_crew = joblib.load(MODELS_DIR / "model_crew.pkl")

def predict_requirements(input_dict: dict):
    # Build DataFrame from input
    X = pd.DataFrame([input_dict])
    X = add_engineered_features(X)

    # Predict using LightGBM models
    pred_hours = float(model_hours.predict(X)[0])
    pred_crew = int(round(model_crew.predict(X)[0]))

    return {
        "predicted_crew_size": pred_crew,
        "predicted_hours_required": pred_hours,
    }
