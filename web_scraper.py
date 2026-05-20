import requests
from bs4 import BeautifulSoup

# Target website
url = "https://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("div", class_="quote")

print("===== SCRAPED DATA =====\n")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    print("Quote:", text)
    print("Author:", author)
    print("-" * 50)