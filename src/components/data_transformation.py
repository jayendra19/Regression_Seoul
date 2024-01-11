import sys
import os
from zenml.steps import BaseParameters
import logging
from abc import ABC,abstractclassmethod
from typing import Union
from typing import Tuple
import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from src.utils import save_object


#from src.utils import save_object

class DataStrategy(ABC):
    '''
    abstract method class defininig strategy for handling data
    #module marks the handle_data() method as an abstract method.Abstract methods don't contain any implementation but are 
    #meant to be overridden in concrete subclasses.'''

    @abstractclassmethod
    def handle_data(self:pd.DataFrame)->Union[pd.DataFrame, pd.Series]:
        '''This class is a template or blueprint for various strategies that handle data. The purpose of this class is to define an interface with a 
common method handle_data() that will be implemented by its subclasses. '''
        pass


class ModelTrainerConfig(BaseParameters):
    trained_model_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataDivideStrategyAndFeatureTransformation(DataStrategy):
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    """Data dividing strategy which divides the data into train and test data."""
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        try:
            # Changing the DATE column to DATE data type
            data['Date'] = pd.to_datetime(data['Date'])
            # Extracting YEAR, MONTHS, AND DAY columns from the DATE COLUMNS
            data['Year'] = data['Date'].dt.year
            data['Day'] = data['Date'].dt.day
            data['Months_name'] = data['Date'].dt.month_name()
            data['Months'] = data['Date'].dt.month
            # Extract the weekday and create a new column
            data['Weekday'] = data['Date'].dt.day_name()

            # Now dropping the DATE column
            data = data.drop(columns='Date',axis=1)
            # Now dropping those columns that we don't want
            data = data.drop(columns=['Humidity(%)', 'Dew point temperature(°C)', 'Months_name'], axis=1)


            X = data.drop("Rented Bike Count", axis=1)
            y = data["Rented Bike Count"]
            logging.info("Seperated from x and y")
            
            # Use ColumnTransformer to handle transformations consistently
            categorical_features = ['Seasons', 'Holiday', 'Functioning Day', 'Weekday']
            numeric_features =  X.select_dtypes(include=[np.number]).columns

            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', StandardScaler(), numeric_features),
                    ('cat', OneHotEncoder(drop='first',handle_unknown='ignore', sparse=False), categorical_features),
                ],
                remainder='passthrough'
            )

            # Create a pipeline with the ColumnTransformer
            pipeline = Pipeline([
                ('preprocessor', preprocessor)
            ])

            # Apply transformations and split the data
            X_transformed = pipeline.fit_transform(X)
            logging.info('Pipeline created and transformed my data ')

            X_train, X_test, y_train, y_test = train_test_split(
                X_transformed, y, test_size=0.2, random_state=42
            )
            logging.info("Divided data into train test and split")

            # Convert NumPy arrays to Pandas DataFrames cuz it won't except 
            X_train_df = pd.DataFrame(X_train, columns=pipeline.named_steps['preprocessor'].get_feature_names_out(X.columns))
            X_test_df = pd.DataFrame(X_test, columns=pipeline.named_steps['preprocessor'].get_feature_names_out(X.columns))
            logging.info('Converted my X_train and my X_test into dataframe')
            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=pipeline)
            
            return X_train_df, X_test_df, y_train, y_test
            

        except Exception as e:
            logging.error(e)
            raise e



















