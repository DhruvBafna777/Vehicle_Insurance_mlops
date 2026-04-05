# from src.logger import logging
# logging.debug("this is Debug message")

# from src.exception import MyException
# from src.logger import logging
# import sys

# try:
#     a = 1/0
# except Exception as e:
#     logging.info("Divide by zero error")
#     raise MyException(e, sys)

from src.pipline.training_pipeline import TrainPipeline
# demo.py

# 1. Initialize your pipeline
pipeline = TrainPipeline()
pipeline.run_pipeline()


