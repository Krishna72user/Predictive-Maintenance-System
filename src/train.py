from logger import logger
from xgboost import XGBClassifier
from config import ConfigManager
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTENC
from sklearn.preprocessing import PowerTransformer,FunctionTransformer,OrdinalEncoder
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score
import joblib
import os
import json

def func(X):
    x = X.copy()
    x["Temperature Difference"] = (
        x["Process temperature [K]"]
        - x["Air temperature [K]"]
    )
    return x
def train():
    try:
        cm = ConfigManager()
        train_params = cm.load_train_params()
        model_params = cm.load_model_params()['RandomForest']
        eval_params = cm.load_eval_params()
        df = pd.read_csv(train_params['train_data'])
        logger.info('Data Loaded Successfully')
        X = df.drop(columns=['Machine failure'],axis =1)

        y = df['Machine failure']
        X_train,X_val,y_train,y_val = train_test_split(X,y,stratify=y,test_size=0.20,random_state=train_params['seed'])
        smote = SMOTENC(random_state=42,categorical_features=['Type'])
        X_train_sampled ,y_train_sampled = smote.fit_resample(X_train,y_train)
        num_types = [
            'Air temperature [K]',
            'Process temperature [K]',
            'Rotational speed [rpm]',
            'Torque [Nm]',
            'Tool wear [min]',
            'Temperature Difference'
        ]
            
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat',OrdinalEncoder(categories=[['L','M','H']],dtype=int),['Type']),
                ('num',PowerTransformer(),num_types)
            ],remainder='passthrough'
        )

        model = RandomForestClassifier(n_estimators=model_params['n_estimators'],
                              max_depth=model_params['max_depth'],
                              max_leaf_nodes=model_params['max_leaf_nodes'],
                              min_samples_leaf = model_params['min_samples_leaf'],
                              max_features=model_params['max_features'],
                              min_samples_split=model_params['min_samples_split']                       
                              )
        pipe = Pipeline(
        steps= [
                ('feature_engg',FunctionTransformer(func)),
                ('preprocessor',preprocessor),
                ('model',model)
            ]
        )
        pipe.fit(X_train_sampled,y_train_sampled)
        logger.info("Model Training Done")
        preds = (pipe.predict_proba(X_val)[:,1]>=.55).astype(int)
        precision = precision_score(y_val,preds)
        accuracy = accuracy_score(y_val,preds)
        recall = recall_score(y_val,preds)
        f1 = f1_score(y_val,preds)
        os.makedirs('models',exist_ok=True)
        os.makedirs('reports',exist_ok=True)

        metrics = {"validation_metrics":{'precision':precision,'recall':recall,'f1-score':f1,'accuracy':accuracy}}

        if os.path.exists(eval_params['path']):
            with open(eval_params['path'], "r") as f:
                all_metrics = json.load(f)
        else: all_metrics=[]
        with open(eval_params['path'],'w') as f:
            all_metrics.extend([metrics])
            json.dump(all_metrics,f)
            logger.info(f"Validation Metrics are saved to {eval_params['path']}")

        joblib.dump(pipe,'models/model.joblib')
        logger.info(f"Pipeline is saved to {train_params['model_path']}")
    except Exception as e:
        logger.exception("Some error occurred in training stage.")


train()
