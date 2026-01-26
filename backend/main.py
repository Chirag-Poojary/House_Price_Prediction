from fastapi import FastAPI
from pydantic import BaseModel
from backend.model_loader import predict_price

app = FastAPI(title="House Price Prediction API")

class HouseFeatures(BaseModel):
    CRIM: float
    ZN: float
    INDUS: float
    CHAS: int
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: int
    TAX: float
    PTRATIO: float
    B: float
    LSTAT: float

@app.post("/predict")
def predict(features: HouseFeatures):
    feature_values = list(features.values())
    prediction = predict_price(feature_values)
    return {"predicted_price": prediction}
