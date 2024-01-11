
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessing='/app/artifacts/preprocessor.pkl'
            model_path='/app/artifacts/model.pkl'
            logging.info(f"Loading object from path: {preprocessing}")

            preprocessing_path=load_object(file_path=preprocessing)
            model=load_object(file_path=model_path)
            data_scaled=preprocessing_path.transform(features)
            pred=model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.error(e)
            raise e
    


class CustomData:
    def __init__(self, hour: int, temperature: float,
             wind_speed_m_s: float, visibility_10m: float,
             solar_radiation_mj_m2: float, rainfall_mm: float, snowfall_cm: float,
             seasons: str, holiday: str, functioning_day: str,
             year: int, day: int, months: int, weekday: str):
         
         self.hour = hour
         self.temperature = temperature
         self.wind_speed_m_s = wind_speed_m_s
         self.visibility_10m = visibility_10m
         self.solar_radiation_mj_m2 = solar_radiation_mj_m2
         self.rainfall_mm = rainfall_mm
         self.snowfall_cm = snowfall_cm
         self.seasons = seasons
         self.holiday = holiday
         self.functioning_day = functioning_day
         self.year = year
         self.day = day
         self.months = months
         self.weekday = weekday

            



    def get_data_as_frame(self):
        try:
            custom_data = {
            "Hour": [self.hour],
            "Temperature(°C)": [self.temperature],
            "Wind speed (m/s)": [self.wind_speed_m_s],
            "Visibility (10m)": [self.visibility_10m],
            "Solar Radiation (MJ/m2)": [self.solar_radiation_mj_m2],
            "Rainfall(mm)": [self.rainfall_mm],
            "Snowfall (cm)": [self.snowfall_cm],
            "Year": [self.year],
            "Day": [self.day],
            "Months": [self.months],
            "Weekday": [self.weekday],
            "Seasons": [self.seasons],  # Include 'Seasons' column
            "Holiday": [self.holiday],  # Include 'Holiday' column
            "Functioning Day": [self.functioning_day],  # Include 'Functioning Day' column
        }
            return pd.DataFrame(custom_data)
            

        except Exception as e:
            logging.error(e)
            raise e
     



        
        

