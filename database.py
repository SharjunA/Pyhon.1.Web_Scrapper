from pymongo import MongoClient
from datetime import datetime
from log_config import logging

def connect_to_mongodb(uri, db_name, collection_name):
    
    # Establishing connection to the MongoDB collection.
    try:
        client = MongoClient(uri)
        db = client[db_name]
        return db[collection_name]
    except Exception as e:
        logging.error(f"Error connecting to MongoDB: {e}")
        return None

def insert_data(collection, data, url):
    
    # Save scraped data to the MongoDB collection.
    try:
        if data:
            
            timestamp = datetime.now()
            document = {
                "Products on NDA": data,
                "Metadata": {
                    "Timestamp": timestamp,
                    "Source URL": url,
                    "Number of Records": len(data)
                }
            }
            
            # Insert the document
            collection.insert_one(document)
            logging.info(f"Successfully inserted {len(data)} drug records with metadata.")
            
    except Exception as e:
        logging.error(f"Error saving data to MongoDB: {e}")