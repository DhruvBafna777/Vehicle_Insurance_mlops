import os 
from datetime import datetime

DB_NAME = 'Vehicle_Proj'
COLLECTION_NAME = 'Vehicle_Insurance'
CONNECTION_URL = 'mongodb+srv://jdhruv282_db_user:MuQPWTswur6zOQvf@cluster1.lg7hwg4.mongodb.net/?appName=Cluster1'

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "Vehicle_Insurance"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.20

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME: str = "model.pkl"

TARGET_COLUMN: str = "Response"
CURRENT_YEAR: int = datetime.now().year
PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing_object.pkl"


FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH: str = os.path.join("config", "schema.yaml")

"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"


"""
Data Transformation realted contant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"



