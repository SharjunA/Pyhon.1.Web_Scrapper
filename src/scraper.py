from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tenacity import retry, stop_after_attempt, wait_fixed
from log_config import logging
from downloader import download_pdfs

@retry(stop = stop_after_attempt(3), wait = wait_fixed(2))
def scrape_data(url):
    driver = None

    try:
        # Initialize Selenium WebDriver
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver.get(url)

        # Wait for the page to load
        #driver.implicitly_wait(10)

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
                
        # Download the data as PDF if required
        download_pdfs(driver)
                   
        return data

    except Exception as e:
        logging.error(f"Error while scraping data: {e}")
        raise
    
    finally:
        # Close the browser
        if driver:
            driver.quit()