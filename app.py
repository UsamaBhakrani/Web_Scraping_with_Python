import requests
from bs4 import BeautifulSoup
response = requests.get('https://stackoverflow.com/questions')
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
