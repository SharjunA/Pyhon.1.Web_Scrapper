from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from log_config import logging

def scrape_data(url):

    try:
        # Initialize Selenium WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)

        # Wait for the page to load
        driver.implicitly_wait(10)

        # Locate the table on the page
        table = driver.find_element(By.TAG_NAME, "table")
        headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Extract data from the table
        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            row_data = {}
            for header, col in zip(headers, cols):
                row_data[header] = col.text
            if row_data:
                data.append(row_data)
                   
        return data

    except Exception as e:
        logging.error(f"Error while scraping data: {e}")
        return []
    
    finally:
        # Close the browser
        driver.quit()