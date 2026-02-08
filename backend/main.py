from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib
from schema.house_features import HouseFeatures

with open('models/stacking_model.pkl', 'rb') as f:
    model = joblib.load(f)

MODEL_VERSION = '1.0.0'

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Boston Housing Price Prediction API"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "version": MODEL_VERSION,
        "model_loaded": model is not None
    }

@app.post("/predict")
def predict(features: HouseFeatures):
    # Convert features to a list for model prediction
    feature_list = [
        features.CRIM, features.ZN, features.INDUS, features.CHAS, features.NOX,
        features.RM, features.AGE, features.DIS, features.RAD, features.TAX,
        features.PTRATIO, features.B, features.LSTAT
    ]
    # Make prediction using the loaded model
    prediction = model.predict([feature_list])[0]
    return JSONResponse(status_code=200, content={"predicted_price": float(prediction)})

