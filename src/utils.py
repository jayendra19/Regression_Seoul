import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dotenv import load_dotenv
import psycopg2
import pickle
import numpy as np

'''use for common funtionality utils'''

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv('database')
port=os.getenv('port')



def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from seoulbike',mydb)
        print(df.head())

        return df



    except Exception as ex:
        raise CustomException(ex,sys)
    




def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        logging.info("Failed to write".format(e))
        raise e
    



def load_object(file_path):
    try:
        # Check if the directory exists
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            raise FileNotFoundError(f"Directory does not exist: {dir_path}")

        # Log the absolute path for debugging
        logging.info(f"Loading object from path: {os.path.abspath(file_path)}")

        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.error(f"Failed to load: {e}")
        raise e