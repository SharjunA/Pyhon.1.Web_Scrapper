import os
import requests
from selenium.webdriver.common.by import By

def download_pdfs(driver, download_dir = "downloads"):
    
    download_choice = input("Would you like to download PDFs? (y/n): ").strip().lower()
        
    if download_choice not in ['y', 'n']:
        print("Invalid input. Please enter 'y' for Yes or 'n' for No.")

    if download_choice.lower() == 'y':
        print("Downloading PDFs...")
    else:
        return
    
    # Ensure the downloads directory exists
    os.makedirs(download_dir, exist_ok=True)

    links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]")
    seen_urls = set()  # Track already downloaded URLs
    
    session = requests.Session()  # Use Session to handle redirects
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    
    for link in links:
        pdf_url = link.get_attribute('href')
        
        # Skip duplicates
        if pdf_url in seen_urls:
            continue
        seen_urls.add(pdf_url)
        
        file_name = os.path.join(download_dir, pdf_url.split('/')[-1])
        
        try:
            response = session.get(pdf_url, allow_redirects=True)
            response.raise_for_status()
            
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
            
        except Exception as e:
            print(f"Failed to download {pdf_url}: {e}")