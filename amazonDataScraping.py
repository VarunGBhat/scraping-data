import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd

product_name = []
product_price = []

# Amazon data Scraping using beautifulSoup and requests
pages_to_scrape = 8
for page in range(1, pages_to_scrape+1):
    url = (
        'https://www.amazon.in/s?k=over-ear+headphones'
        f'&page={page}&crid=26DOX8DP34WTI&qid=1749199512&sprefix=over-ear+hea%2Caps%2C1822&xpid=lJ2W6ugTdA5V0&ref=sr_pg_{page}'

    )

    # Headers to mimic a real browser
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
    }

    # Send the request
    response = requests.get(url, headers=custom_headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'lxml')

    # Find all product containers
    product_boxes = soup.find_all('div', {'data-component-type': 's-search-result'})

    # Loop through each product and extract the title
    for box in product_boxes:
        title_tag = box.find('h2')
        title_price = box.find('span', {'class': 'a-price-whole'})
        if title_tag and title_price:
            product_name.append(title_tag.text.strip())
            product_price.append(title_price.text.strip() if title_price else 'Price not available')

    # Print status code
    print("Status Code:", response.status_code)

# store the product name in the csv file
df = pd.DataFrame({"Product Name": product_name, "Product Price": product_price})

# Adjust the path as required
df.to_csv(r"D:\webscraping\AmazonData.csv", index=False)
