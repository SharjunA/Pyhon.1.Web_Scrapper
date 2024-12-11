from scraper import scrape_data
from database import connect_to_mongodb, insert_data
from log_config import logging

def main():

    try:
        url = "https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=020892"
        
        # Scrape data
        print("Starting the scraping process...")
        scraped_data = scrape_data(url)
        if not scraped_data:
            print("No data scraped.")
            return

        print("Data scraped successfully. Saving to MongoDB...")
        # MongoDB connection and data storage
        collection = connect_to_mongodb(
            uri = "mongodb://localhost:27017/",
            db_name = "drug_data",
            collection_name = "drug_info"
        )
        
        if collection is not None:
            insert_data(collection, scraped_data, url)
        
        print("Data saved to MongoDB Collection successfully.")
                        
    except Exception as e:
        logging.error(f"Scraping failed after maximum retries: {e}")
        print("Scraping process not completed. Check logs for details.")
    
    
if __name__ == "__main__":
    main()