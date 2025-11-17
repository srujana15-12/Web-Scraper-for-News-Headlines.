import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"  # example website
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for h in soup.find_all("h2"):
    text = h.get_text(strip=True)
    if text:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as f:
    for line in headlines:
        f.write(line + "\n")

print("Scraping complete. Headlines saved to headlines.txt")
