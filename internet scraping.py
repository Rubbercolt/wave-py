import requests
from bs4 import BeautifulSoup

url = 'https://www.tvcnews.tv/politics/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for news in soup .find_all('article'):
    title = news .find('h3').text.strip()
    if title:
        print(title)
    else:
        print("Headline not found")
    img = news.find('img')
    if img:
        image = img.get('src')
        print(f'https:{image}')
    else:
        print("image not found")
    li = news.find('a')
    if li:
        link = li.get('href')
        print(link)
    else:
        print('url not found')
    print("\n")