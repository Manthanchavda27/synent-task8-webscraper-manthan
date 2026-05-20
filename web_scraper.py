import requests
from bs4 import BeautifulSoup
import csv

# Target website
url = "https://quotes.toscrape.com"

try:
    # Send request
    response = requests.get(url)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all quotes
    quotes = soup.find_all("div", class_="quote")

    print("===== SCRAPED DATA =====\n")

    # Create CSV file
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text

            print("Quote:", text)
            print("Author:", author)
            print("-" * 50)

            # Write to CSV
            writer.writerow([text, author])

    print("\nData successfully saved to scraped_data.csv")

except requests.exceptions.RequestException as e:
    print("Error fetching website:", e)