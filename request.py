import requests
row_text = requests.get('https://docs.djangoproject.com/en/4.2/topics/db/queries/').text
from bs4 import BeautifulSoup
soup = BeautifulSoup(row_text)
soup.find('div', {'id': 'docs-content'}).text
print(soup)
print(row_text)
