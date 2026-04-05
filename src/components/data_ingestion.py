import os 
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import MyException
from src.logger import logging
from src.data_access.proj1_data import Proj1Data

class DataIngestion:
    
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            logging.error(f"Error occurred in Data Ingestion class constructor: {e}")
            raise MyException(e, sys) from e
        
    def export_data_into_feature_store(self, dataframe: DataFrame) -> str:
        try:
            logging.info("Exporting data into feature store")
            mydata = Proj1Data()
            dataframe = mydata.export_data_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            
            logging.info(f"Shape of DataFrame : {dataframe.shape}")
            feature_store_file_path  = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe

        except Exception as e:
            raise MyException(e,sys)
        
    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        try:
            logging.info("Splitting data into train and test set")
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42)
            
            logging.info(f"Saving train and test data into file path: {self.data_ingestion_config.training_file_path} and {self.data_ingestion_config.test_file_path}")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)
            
            logging.info("Data split into train and test set successfully")
            
        except Exception as e:
            logging.error(f"Error while splitting data into train and test set: {e}")
            raise MyException(e, sys) from e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store(dataframe=None)
            logging.info("Got the dataframe from mongoDB")
            
            self.split_data_as_train_test(dataframe=dataframe)
            
            logging.info("Performed Train Test Split on the dataset")
            
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
            test_file_path=self.data_ingestion_config.test_file_path)
            
            logging.info(f"Data Ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            logging.error(f"Error occurred in initiate_data_ingestion method: {e}")
            raise MyException(e, sys) from e