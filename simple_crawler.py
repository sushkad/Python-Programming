import requests
from bs4 import BeautifulSoup

url = "https://agreeable-meadow-0eb877f1e.6.azurestaticapps.net/pipeline-zone/2/32/tested"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get page title
print("Page Title:", soup.title.string if soup.title else "No Title")

# Get all links
print("\nAll Links on Page:")
for link in soup.find_all("a"):
    print(link.get("href"))
