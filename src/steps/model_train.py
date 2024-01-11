from src.logger import logging
import pandas as pd
from zenml import step
from src.components.model_trainer import Xgboost
from sklearn.base import RegressorMixin
from src.steps.config import ModelNameConfig
import mlflow
from zenml.client import Client

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def train_model(X_train:pd.DataFrame,
                X_test:pd.DataFrame,
                y_train:pd.Series,
                y_test:pd.Series,
                config: ModelNameConfig,
               )->RegressorMixin:
    '''-> RegressorMixin: The function is expected to return an object that adheres to the RegressorMixin interface from scikit-learn. 
    This typically represents a trained regression model or an object with regression-related functionalities.
    '''
    try:
        model = None

        if config.model_name == "xgboost":
            mlflow.xgboost.autolog()
            model = Xgboost()
            trained_model = model.train(X_train, y_train)
            logging.info("Trained the model susccesfully on X_train and y_train")
            




        return trained_model
    


    except Exception as e:
        logging.error(e)
        raise e
    

















