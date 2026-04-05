import sys
import pandas as pd
import numpy as np 
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBConnection
from src.constants import DB_NAME
from src.exception import MyException
from src.logger import logging

class Proj1Data:
    def __init__(self) -> None:
        try:
            self.mongo_db_connection = MongoDBConnection()
        except Exception as e:
            raise MyException(e, sys) from e
        
    def export_data_as_dataframe(self, collection_name: str, DB_NAME: Optional[str] = None) -> pd.DataFrame:
        try:
            if DB_NAME is None:
                collection = self.mongo_db_connection.database[collection_name]
            else:
                collection = self.mongo_db_connection.client[DB_NAME][collection_name]
                
            print(f"Exporting data from collection: {collection_name} in database: {DB_NAME if DB_NAME else self.mongo_db_connection.database_name}")
            logging.info(f"Exporting data from collection: {collection_name} in database: {DB_NAME if DB_NAME else self.mongo_db_connection.database_name}")
            df = pd.DataFrame(list(collection.find()))
            
            if 'id' in df.columns:
                df.drop(columns=['id'], inplace=True)
                
            df.replace({np.nan: None}, inplace=True)
            logging.info(f"Data exported successfully from collection: {collection_name}")
            return df
        
        except Exception as e:
            logging.error(f"Error while exporting data from MongoDB: {e}")
            raise MyException(e, sys) from e    