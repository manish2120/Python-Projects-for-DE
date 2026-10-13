import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/health_47/index.html"
response = requests.get(url)

# html.parser to parse to convert the raw HTML into a structured format (parse tree)
# .text attribute of response object returns HTML content of the page as a string.
soup = BeautifulSoup(response.text, "html.parser")

if response.status_code == 200:
  article = soup.find('article')
  heading = article.find('h3')
  anchor = heading.find('a')
  title = anchor.get("title")

  data = []
  books = soup.find_all("article", class_="product_pod")
  for book in books:
    title = book.h3.a['title']
    product = book.find('p', class_="product_price")
    price = book.find('p', class_="price_color").get_text(strip=True)
    availability = book.find('p', class_="instock availability").get_text(strip=True)
    data.append(
      {
        "name": title,
        "price": price,
        "availability": availability
      }
    )

  df = pd.DataFrame(data) # this automatically converts the keys into column headers and values as values of those columns
  df.to_csv("books.csv", index=False)
  print(df.head())