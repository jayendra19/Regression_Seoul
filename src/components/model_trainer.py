import sys
import os
from src.logger import logging
from src.exception import CustomException
from abc import ABC,abstractmethod
import xgboost as xgb
from xgboost import XGBRegressor
from zenml.steps import BaseParameters
from src.utils import save_object





class Model(ABC):

    @abstractmethod
    def train(self,X_train,y_train):
        pass



class ModelTrainerConfig(BaseParameters):
    trained_model_file_path=os.path.join("artifacts","model.pkl")


class Xgboost(Model):
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    """XGBoostModel that implements the Model interface."""


    def train(self, X_train, y_train,**kwargs):
        '''**kwargs allows passing additional optional arguments to configure the xgboost Regression model. 
        These can include parameters like fit_intercept, normalize, etc., which are specific to the LinearRegression class.'''
        try:
            reg=XGBRegressor(subsample=0.79,
                       n_estimators=1000,
                       max_depth=7,
                       learning_rate=0.1,
                       colsample_bytree=0.8999999999999999,
                       colsample_bylevel=0.4,seed=20)
            '''directly prociding best parameteres from notebooks '''
            reg.fit(X_train,y_train)
            logging.info('xgboost model got trained')

            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=reg)
            logging.info("saved the model as pickle file ")
            return reg
    
        except Exception as e:
            logging.error(e)
            raise e
        









