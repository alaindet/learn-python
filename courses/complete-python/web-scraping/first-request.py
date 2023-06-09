import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.example.com')
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('h1').string
print(title) # Example Domain
