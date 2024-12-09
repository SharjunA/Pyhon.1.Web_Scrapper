import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_data():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    
    data = []
    url = 'https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=020892'
    page = requests.get(url, headers=headers, allow_redirects=True)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    print(soup.prettify())
    
    # #accessing the table
    # table = soup.find('table', {'class' : 'table table-bordered dataTable no-footer dtr-inline collapsed'})
    # #extracting all rows
    # rows = table.find_all('tr')
    
    # for row in rows:
    #     cells = row.find_all('td')  # Extract all cells
    #     print([cell.text.strip() for cell in cells])
        
scrape_data()
    #     if cells:
    #         record = {
    #             "drug_name": cells[0].text.strip(),
    #             "active_ingredient": cells[1].text.strip(),
    #             "strength": cells[2].text.strip(),
    #         }
    #         data.append(record)

    # # Add metadata
    # for record in data:
    #     record["metadata"] = {
    #         "timestamp": datetime.utcnow().isoformat(),
    #         "source_url": url
    #     }
    # return data