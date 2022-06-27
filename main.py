import requests
from bs4 import BeautifulSoup

content = requests.get('https://kalam.sindonews.com/jadwalsholat')


soup = BeautifulSoup(content.text, 'html.parser')
title = (soup.find('title')).text
print(title)

