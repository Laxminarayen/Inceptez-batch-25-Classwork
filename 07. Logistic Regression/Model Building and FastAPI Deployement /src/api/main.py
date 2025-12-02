from typing import Union
import joblib
from fastapi import FastAPI
from custom_model_pipeline import ThresholdClassifier
import pandas as pd
import numpy as np
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()


class ModelInfo(BaseModel):
    """ Model information structure."""
    model_name: str
    model_type: str
    model_version: str
    model_features: list[str]
    model_author: str
    model_description: str
    model_accuracy: float
    model_precision: float
    model_recall: float
    model_f1: float


class PredictReuest(BaseModel):
    """ Prediction request structure."""
    ID: str
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int


class PredictResponse(BaseModel):
    """ Prediction response structure."""
    patient_id: str
    prediction_class: str
    prediction: int
    probability: float
    timestamp: str


def load_model():
    global model
    model = joblib.load("../../models/model_balanced_threshold_0.45.pkl")
    return model


@app.on_event("startup")
def startup_event():
    load_model()
    print("Model loaded successfully")




@app.get("/", tags=["Root"])
def read_root():
    """ Root endpoint returning a information.
    """
    return {
        "mesage": "Welcome to the Sepsis Prediction API. Use the /predict endpoint to get predictions.",
        "version": "1.0.0",
        "author": "Noordeen",
        "status": "development environemnt",
        "endpoints":{
            "docs": "/docs",
            "redoc": "/redoc",
            "model_info": "/model_info",
            "predict":"/predict"
        }

    }
    

@app.get("/model_info")
def get_model_info() -> ModelInfo:
    """" Endpoint to get model information."""
    if model is None:
        return {"error": "Model not loaded"}
    else:
        return ModelInfo(
                model_name="Sepsis Prediction Model",
                model_type = "Logistic Regression with Threshold Classifier",
                model_version = "1.0.0",
                model_features = ['ID', 'PRG', 'PL', 'PR', 'SK', 'TS', 'M11', 'BD2', 'Age', 'Insurance','Sepssis'],
                model_author = "Noordeen",
                model_description = "A logistic regression model to predict sepsis in patients using a custom threshold classifier to handle class imbalance.",
                model_accuracy = 0.68,
                model_precision = 0.54,
                model_recall = 0.79,
                model_f1 = 0.64
            )
    

@app.post("/predict")
def predict(data: PredictReuest) -> PredictResponse:
    """ Endpoint to get predictions."""
    if model is None:
        return {"error": "Model not loaded"}
    else:
        data = data.dict()
        patient_id = data.pop("ID")
        data = pd.DataFrame([data])
        prediction = model.predict(data)
        probability = model.predict_proba(data)[0][1]
        prediction_class = "Positive" if prediction[0] == 1 else "Negative"
        return PredictResponse(
            patient_id=patient_id,
            prediction_class=prediction_class,
            prediction=prediction[0],
            probability=probability,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )