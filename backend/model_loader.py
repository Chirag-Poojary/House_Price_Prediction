import joblib
from pathlib import Path

MODEL_PATH = Path("./models/stacking_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_price(features):
    return model.predict([features])[0]
