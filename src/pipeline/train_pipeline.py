import mlflow
from zenml.pipelines import pipeline
from src.steps.ingest_data import ingest_df
from src.steps.clean_data import clean_df
from src.steps.model_train import train_model
from src.steps.evaluation import evaluate_model
from src.components.data_ingestion import DataIngestion
@pipeline(enable_cache=True)
def training_pipeline():
    with mlflow.start_run():
        try:
            data_ingestion = DataIngestion()
            raw_data_path = data_ingestion.initiate_data_ingestion()

            # Pass raw_data_path to ingest_data
            df = ingest_df(data_path=raw_data_path)
            
            X_train, X_test, y_train, y_test = clean_df(df)

            # Create a ModelNameConfig instance and pass it to train_model
            model = train_model(X_train, X_test, y_train, y_test)

            # Log metrics
            r2_score, mse, rmse = evaluate_model(model, X_test, y_test)

            return r2_score, mse, rmse

        finally:
            mlflow.end_run()


        
        

        
        
            
    

    
    


        
        
        
        


