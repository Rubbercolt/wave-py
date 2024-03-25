import requests
from bs4 import BeautifulSoup

base_url =' https://www.arise.tv/category/entertainment/'
re = requests.get(base_url)
pg_content = BeautifulSoup(re.text, 'html.parser')
for data in pg_content.find_ all('article'):
    for data 
