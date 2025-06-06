# Web Scraping Project: Amazon & Flipkart Product Data

This project contains Python scripts to scrape product data from Amazon and Flipkart, as well as a script to download PDF files from a specified website. The data is saved in CSV files for further analysis.

## Project Structure

- `amazonDataScraping.py`: Scrapes over-ear headphone product names and prices from Amazon India.
- `flipkartDataScraping.py`: Scrapes laptop product names, prices, ratings, and number of reviews from Flipkart.
- `toDownloadTheFileScraping.py`: Downloads all PDF files listed on a specific academic webpage.
- `AmazonData.csv`: Output file containing scraped Amazon product data.
- `FlipkartData.csv`: Output file containing scraped Flipkart product data.

## Requirements

- Python 3.12+
- Packages:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `lxml`

Install dependencies with:

```sh
pip install requests beautifulsoup4 pandas lxml
```

## Usage

### 1. Scrape Amazon Data

Run the following command to scrape over-ear headphone data from Amazon and save it to `AmazonData.csv`:

```sh
python amazonDataScraping.py
```

### 2. Scrape Flipkart Data

Run the following command to scrape laptop data from Flipkart and save it to `FlipkartData.csv`:

```sh
python flipkartDataScraping.py
```

### 3. Download Academic PDFs

Run the following command to download all PDF files from the specified academic webpage:

```sh
python toDownloadTheFileScraping.py
```

## Output

- `AmazonData.csv`: Contains columns `Product Name` and `Product Price`.
- `FlipkartData.csv`: Contains columns `Product Name`, `Prices`, `Rating`, and `Number of Review`.
- Downloaded PDF files will be saved in the current directory.

## Notes

- The scripts use custom headers and cookies to mimic browser requests.
- Be mindful of the website's terms of service and robots.txt before scraping.
- The output CSV file paths in the scripts may need to be adjusted based on your environment.

## License

This project is for educational purposes only.
