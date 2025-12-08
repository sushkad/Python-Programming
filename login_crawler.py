import requests
from bs4 import BeautifulSoup

# 1. Create a session (persists cookies)
session = requests.Session()

# 2. Set login URL
login_url = "https://jolly-pebble-0999b071e.6.azurestaticapps.net/login"

# 3. Prepare credentials (replace with valid ones)
payload = {
    "username": "vijayjain@amsysis.com",   # adjust key to actual <input name="">
    "password": "Vijay@123"
}

# 4. Send POST request to login
response = session.post(login_url, data=payload)

# 5. Check if login was successful
if "Logout" in response.text or "CyberHook" in response.text:
    print("✅ Login successful!")
else:
    print("⚠️ Login might have failed. Check credentials/field names.")

# 6. Access a protected page (example: dashboard)
protected_url = "https://jolly-pebble-0999b071e.6.azurestaticapps.net/"
res = session.get(protected_url)
soup = BeautifulSoup(res.text, "html.parser")

print("\nPage Title:", soup.title.string if soup.title else "No title found")
