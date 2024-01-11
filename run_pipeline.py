from src.pipeline.train_pipeline import training_pipeline
from zenml.client import Client

import mlflow


if __name__ == "__main__":
    try:
        # Start a new run
        # Call your training pipeline
        print(Client().active_stack.experiment_tracker.get_tracking_uri())
        training = training_pipeline()
        training.run()

    except Exception as e:
        print(f"Error: {e}")





