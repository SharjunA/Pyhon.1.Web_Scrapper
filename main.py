from bs4 import BeautifulSoup
import requests

url = 'https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=020892'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')

print(soup)