# webcrawling


import requests
from bs4 import BeautifulSoup

url = "https://jolly-pebble-0999b071e.6.azurestaticapps.net/login"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
print(soup.title.text)   # Extract page title
