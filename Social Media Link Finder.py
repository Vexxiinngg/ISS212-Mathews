#Lauren Mathews
#Social Media Finder
#Resources- Jen moody past scripts and ChatGPT
import requests
from bs4 import BeautifulSoup

#The website that will be scanned
url = "https://www.Data.gov"

#List of the platforms that will be looked for
platforms = ["facebook.com", "twitter.com", "instagram.com", "youtube.com", "github.com"]

#Makes a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Opens the file to save the results
with open(".venv/social_links.txt", "w") as file:
    file.write(f"Socail Media link found {url}:\n\n")

    #Goes through every page link
    for link in soup.find_all('a', href=True):
        href = link['href']
        for platform in platforms:
            if platform in href:
                file.write(href + "\n")
                print("Found", href)

#Prints the message of what links associated were found
print("Social media link have been saved to social_links.txt")
