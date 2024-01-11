import logging
import pandas as pd
from zenml import step
import pandas as pd
from zenml import step
from src.logger import logging
from zenml.client import Client
experiment_tracker = Client().active_stack.experiment_tracker


class IngestData:
    """
    Data ingestion class which ingests data from the source and returns a DataFrame.
    """

    def __init__(self, data_path: str):
        """Initialize the data ingestion class."""
        self.data_path = data_path

    def get_data(self) -> pd.DataFrame:
         return pd.read_csv(self.data_path)
        
    


@step(experiment_tracker=experiment_tracker.name)
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Args:
        data_path: str
    Returns:
        df: pd.DataFrame
    """
    try:
        ingest_data = IngestData(data_path)

        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(e)
        raise e
