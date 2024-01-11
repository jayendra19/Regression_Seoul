import logging
import sys
from src.exception import CustomException
from zenml import step
import pandas as pd
from src.components.evaluation import MSE,R2Score,RMSE
from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated
from zenml.client import Client
import mlflow


experiment_tracker = Client().active_stack.experiment_tracker
@step(experiment_tracker=experiment_tracker.name)
def evaluate_model(model:RegressorMixin,
                   X_test:pd.DataFrame,
                   y_test:pd.Series,) -> Tuple[
                           Annotated[float,"r2_score"],
                           Annotated[float,"rmse"],
                           Annotated[float,"mse"],
                   ]:
        # Classes that implement this mixin should contain methods related to regression tasks, such as fit() and predict().
        #if u see -> known as function annotations or type hints, is used to specify the expected type of the return value from a function or method. > int indicates that the function will return an integer.
        """evaluates the model on the ingested data args:df:the ingested data """
        try:
                prediction=model.predict(X_test) 
                mse_class=MSE()
                mse=mse_class.calculate_score(y_test,prediction)
                mlflow.log_metric("mse", mse)
                logging.info("mse done")
    

                r2_class=R2Score()
                r2_score= r2_class.calculate_score(y_test,prediction)
                mlflow.log_metric("r2_score", r2_score)
                logging.info("r2_score done")
                

                rmse_class=RMSE()
                rmse=rmse_class.calculate_score(y_test,prediction)
                mlflow.log_metric("rmse", rmse)
                logging.info("rmse_score done")


                
            

                return r2_score,rmse,mse
        
        except Exception as e:
                logging.error(e)
                raise e


























