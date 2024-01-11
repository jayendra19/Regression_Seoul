import sys
from src.exception import CustomException
from src.logger import logging
import logging
from abc import ABC,abstractclassmethod
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

class Evaluate(ABC):


    @abstractclassmethod
    def calculate_score(self,y_test:np.ndarray,y_pred:np.ndarray)->float:
        pass


class MSE(Evaluate):
    def calculate_score(self,y_test:np.ndarray,y_pred:np.ndarray)->float:
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            mse: float
        """

        try:
            logging.info("Entered the calculate_score method of the MSE class")
            mse = mean_squared_error(y_test, y_pred)
            logging.info("the mean squared value is MSE: {}".format(mse))
            return mse
        except Exception as e:
            raise CustomException(e, sys.exc_info())
        



class R2Score(Evaluate):
    
    def calculate_score(self, y_test: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            r2_score: float
        """
        try:
            logging.info("Entered the calculate_score method of the R2Score class")
            r2 = r2_score(y_test, y_pred)
            logging.info("The r2_score value is: " + str(r2))
            return r2
        except Exception as e:
            logging.error(
                "Exception occurred in calculate_score method of the R2Score class. Exception message:  "
                + str(e))
            raise e
        

class RMSE(Evaluate):


    def calculate_score(self, y_test: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Args:
            y_true: np.ndarray
            y_pred: np.ndarray
        Returns:
            rmse: float
        """
        try:
            logging.info("Entered the calculate_score method of the RMSE class")
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            logging.info("The root mean squared error value is: " + str(rmse))
            return rmse
        except Exception as e:
            logging.error(
                "Exception occurred in calculate_score method of the RMSE class. Exception message:  "+ str(e))
            raise e
























