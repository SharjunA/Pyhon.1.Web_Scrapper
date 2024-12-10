import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import log_config

def scrape_data(url):

    try:
        # Initialize Selenium WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)

        # Wait for the page to load
        driver.implicitly_wait(10)

        # Locate the table on the page
        table = driver.find_element(By.TAG_NAME, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Extract data from the table
        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            data.append([col.text.strip() for col in cols])

        driver.quit()  # Close the browser
        return data

    except Exception as e:
        logging.error(f"Error while scraping data: {e}")
        return []