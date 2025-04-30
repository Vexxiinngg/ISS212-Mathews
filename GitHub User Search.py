#Lauren Mathews
#Resources Jen Moody
import requests

# Search for GitHub users based on a keyword
keyword = "EthicalHacker"
url = f"https://api.github.com/search/users?q={keyword}&per_page=5"

# Sends the request
response = requests.get(url)
data = response.json()

# Process and print results
for user in data.get("items", []):
    print("Username:", user["login"])
    print("Profile URL:", user["html_url"])
    print("User ID:", user["id"])
    print("-" * 40)