import yaml
from logger import logger

class ConfigManager:
    def __init__(self,base_path='./params.yaml'):
        self.base_path = base_path
        logger.info("ConfigManager Initialized")
    def load_model_params(self):
        try:
            with open(self.base_path,'r') as f:
                params = yaml.safe_load(f)['model']
                logger.info("Model Parameters Loaded")
                return params
        except Exception as e:
            logger.exception("Some error occurred during loading model params")
    def load_train_params(self):
        try:
            with open(self.base_path,'r') as f:
                params = yaml.safe_load(f)['train']
                logger.info("Training Parameters Loaded")
                return params
        except Exception as e:
            logger.exception("Some error occurred during loading training params")
    def load_data_params(self):
        try:
            with open(self.base_path,'r') as f:
                params = yaml.safe_load(f)['data']
                logger.info("Data Parameters Loaded")
                return params
        except Exception as e:
            logger.exception("Some error occurred during loading data params")
    def load_process_params(self):
        try:
            with open(self.base_path,'r') as f:
                params = yaml.safe_load(f)['preprocess']
                logger.info("Preprocessing Parameters Loaded")
                return params
        except Exception as e:
            logger.exception("Some error occurred during loading process params")
    def load_eval_params(self):
        try:
            with open(self.base_path,'r') as f:
                params = yaml.safe_load(f)['evaluation']
                logger.info("Evaluation Parameters Loaded")
                return params
        except Exception as e:
            logger.exception("Some error occurred during loading evaluation params")
        