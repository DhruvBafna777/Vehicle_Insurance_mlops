import os 
import sys
import pymongo
import certifi

from src.constants import CONNECTION_URL, DB_NAME, COLLECTION_NAME
from src.exception import MyException
from src.logger import logging

ca = certifi.where()

class MongoDBConnection:
    
    client = None
    def  __init__(self):
        try:
            if MongoDBConnection.client is None:
                
                Mongo_DB_Url = CONNECTION_URL
                if Mongo_DB_Url is None:
                    raise MyException("MongoDB connection URL is not provided", sys)
            
                MongoDBConnection.client = pymongo.MongoClient(CONNECTION_URL, tlsCAFile=ca)
            
            
            self.client = MongoDBConnection.client
            self.database = self.client[DB_NAME]  # Connect to the specified database
            self.database_name = DB_NAME
            logging.info("MongoDB connection successful.")
            
        except Exception as e:
            logging.error(f"Error while connecting to MongoDB: {e}")
            raise MyException(e, sys)