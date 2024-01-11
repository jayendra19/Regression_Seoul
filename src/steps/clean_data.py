import logging
import pandas as pd

from src.components.data_transformation import DataDivideStrategyAndFeatureTransformation
from typing import Tuple
from zenml import step
from typing_extensions import Annotated




    
@step
def clean_df(data: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame,"X_train"],
    Annotated[pd.DataFrame,"X_test"],
    Annotated[pd.Series,"y_train"],
    Annotated[pd.Series,"y_test"],]:
    
    try:
        
        divide_strategy = DataDivideStrategyAndFeatureTransformation()
        x_train, x_test, y_train, y_test = divide_strategy.handle_data(data)
        logging.info("Divide_strategy has been done")

        return x_train, x_test, y_train, y_test

        
    except Exception as e:
        logging.error(e)
        raise e











