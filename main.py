from scraper import scrape_data
from database import insert_data

if __name__ == '__main__':
    data = scrape_data()
    
    if data:
        insert_data("NDA_Products", data) 