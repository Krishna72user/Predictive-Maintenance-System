import joblib
import pandas as pd
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
import json
from config import ConfigManager
from logger import logger
import os

def evaluate():
    try:
        cm = ConfigManager()
        train_params = cm.load_train_params()
        data_params = cm.load_data_params()
        eval_params = cm.load_eval_params()
        df = pd.read_csv(data_params['test_path'])
        logger.info('Test Data Loaded Successfully')
        X = df.drop(columns=['Machine failure'],axis =1)
        y = df['Machine failure']

        model = joblib.load(train_params['model_path'])
        logger.info("Model Loaded Successfully")
        preds = (model.predict_proba(X)[:,1]>=eval_params['threshold']).astype(int)

        acc = accuracy_score(y,preds)
        pr = precision_score(y,preds)
        rec = recall_score(y,preds)
        f1 = f1_score(y,preds)
        os.makedirs('reports',exist_ok=True)
        metrics = {"test_metrics":{'precision':pr,'recall':rec,'f1-score':f1,'accuracy':acc}}

        if os.path.exists(eval_params['path']):
            try:
                with open(eval_params['path'], "r") as f:
                    all_metrics = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                all_metrics = []
        else:
            all_metrics = []

        all_metrics.append(metrics)

        with open(eval_params['path'], "w") as f:
            json.dump(all_metrics, f, indent=4)

        logger.info(
            f"Testing Metrics are saved to {eval_params['path']}"
        )
       
    except Exception as e:
        logger.exception("Some error occurred in evaluation stage.")

evaluate()