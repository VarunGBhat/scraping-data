import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# Initialize empty lists to store the extracted data
Product_name = []
Prices = []
Rating = []
Num_review = []

Pages_to_scrape = 5

# Loop through the pages to scrape the data
for page in range(1, Pages_to_scrape + 1):

    custom_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
    }
    url = f"https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}"

    # Send a request to the URL to get the page's content.
    request = requests.get(url, headers=custom_headers)

    # Parse the HTML content using BeautifulSoup.
    soup = BeautifulSoup(request.text, "lxml")

    print(request.status_code)

    if request.status_code > 300:
        continue

    # Find the container that holds the individual products.
    container = soup.find("div", class_="DOjaWF gdgoEp")
    Products = container.find_all("div", class_="_75nlfW")

    # Extract information for each product in the container and store into the initialized empty list.
    for Product in Products:
        try:
            name = Product.find("div", class_="KzDlHZ").text.strip()
        except:
            name = " "
        Product_name.append(name)

        try:
            price = Product.find("div", class_="Nx9bqj _4b5DiR").text.strip()
            price = price.replace("₹", "").replace(",", "")
        except:
            price = " "
        Prices.append(price)

        try:
            rating = Product.find("div", class_="XQDdHH").text.strip()
        except:
            rating = "Not Available"
        Rating.append(rating)

        try:
            # Find the parent element containing both ratings and reviews
            review_parent = Product.find("span", class_="hG7V+4")
            if review_parent:
                # Get the next sibling span, which contains the reviews text
                reviews_span = review_parent.find_next_sibling("span")
                if reviews_span:
                    n_review = reviews_span.text.strip().split()[0].replace(",", "")
                else:
                    n_review = "0"
            else:
                n_review = "0"
        except:
            n_review = "0"
        Num_review.append(n_review)

    # Add a delay to avoid overloading the server with too many requests.
    time.sleep(2)

# Create a DataFrame from the extracted data and Save the DataFrame to a CSV file.
df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Rating": Rating,
                   "Number of Review": Num_review})
df.to_csv(r"C:\webscraping\FlipkartData.csv", index=False)
