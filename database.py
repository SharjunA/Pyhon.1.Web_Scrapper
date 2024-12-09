from pymongo import MongoClient

def get_database():
    client = MongoClient('mongodb://localhost:27017')
    return client['NDA_Data']

def insert_data(collection_name, data):
    db = get_database()
    collection = db[collection_name]
    
    if isinstance(data, list):  # If data is a list for multiple documents
        collection.insert_many(data)
        print(f"Inserted {len(data)} records into {collection_name}.")
    else:  # For single document
        collection.insert_one(data)
        print(f"Inserted one record into {collection_name}.")