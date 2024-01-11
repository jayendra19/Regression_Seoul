
from src.logger import logging


import traceback

class CustomException(Exception):
    def __init__(self, error, error_detail=None):
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message

def error_message_detail(error, error_detail=None):
    if error_detail is None:
        error_detail = traceback.format_exc()
    return f"Error occurred: {str(error)}\n{error_detail}"


