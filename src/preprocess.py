import pandas as pd
import os
from config import ConfigManager
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTENC
from logger import logger

def preprocess():
    try:
        
        cm = ConfigManager()
        data_params = cm.load_data_params()
        process_params = cm.load_process_params()
        df = pd.read_csv(data_params['raw_path']).iloc[:,2:9]
        logger.info("Data Loaded Succesfully")
        X = df.drop('Machine failure',axis = 1)
        y = df['Machine failure']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=process_params['split'],stratify=y,random_state=process_params['seed'])
        X_train_res,y_train_res = SMOTENC(random_state=process_params['seed'],categorical_features=['Type']).fit_resample(X_train,y_train)
        os.makedirs('./data/processed',exist_ok=True)
        processed_train = pd.concat((X_train_res,y_train_res),axis=1)
        processed_train.to_csv(f'{data_params['train_path']}',index=False)
        processed_test = pd.concat((X_test,y_test),axis = 1)
        processed_test.to_csv(f'{data_params['test_path']}',index=False)
        logger.info("Data preprocessing done")


    except Exception as e:
        logger.exception("Some error occured in preprocessing stage. ")


preprocess()