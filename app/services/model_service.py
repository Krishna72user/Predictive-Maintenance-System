import os
import joblib
from app.core.config import settings
from fastapi import HTTPException
from app.schemas.inference import InferenceModel
import pandas as pd

def load_model():
    try:
        path = settings.model_path
        if  os.path.exists(path):
            model = joblib.load(path)
            return model
    except Exception as e:
        raise HTTPException(
                    status_code=500,
                    detail=f"An unexpected error occurred while loading the model.",
                )



def prediction(query:InferenceModel,model):

    temp_diff = query.process_temp-query.air_temp
    data = query.model_dump()
    data['temp_diff'] = temp_diff
    X=pd.DataFrame([data.values()],columns = [
    'Type',
    'Air temperature [K]',
    'Process temperature [K]',
    'Rotational speed [rpm]',
    'Torque [Nm]',
    'Tool wear [min]',
    'Temperature Difference'
    ])
    probs = model.predict_proba(X)
    return probs
    