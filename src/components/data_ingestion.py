import os
from src.logger import logging
import pandas as pd
from src.utils import read_sql_data
from zenml import step
#from dataclasses import dataclass
from zenml.steps import BaseParameters
import mlflow

class DataIngestionConfig(BaseParameters):
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    '''DataIngestion class seems to be designed to handle the ingestion of data,
    including reading data from MySQL, saving it to CSV files,
    and splitting it into train and test sets. '''

    def __init__(self):
        # Initialize the DataIngestionConfig
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # Reading the data from MySQL
            df = read_sql_data()
            logging.info("Reading completed MySQL database")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save raw data to CSV
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)


            logging.info("Raw Data Ingestion is completed")

            return self.ingestion_config.raw_data_path

        except Exception as e:
            logging.error(e)
            raise e
