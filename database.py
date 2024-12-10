import logging
from pymongo import MongoClient
import log_config

def connect_to_mongodb(uri, db_name, collection_name):
    
    # Establishing connection to the MongoDB collection.
    try:
        client = MongoClient(uri)
        db = client[db_name]
        return db[collection_name]
    except Exception as e:
        logging.error(f"Error connecting to MongoDB: {e}")
        return None

def insert_data(collection, data):
    
    # Save scraped data to the MongoDB collection.
    try:
        if data:
            formatted_data = [{"Drug Info": row} for row in data]
            collection.insert_many(formatted_data)
            logging.info(f"Successfully inserted {len(data)} records.")
        else:
            logging.warning("No data provided to save.")
    except Exception as e:
        logging.error(f"Error saving data to MongoDB: {e}")