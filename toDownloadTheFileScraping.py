import requests
from bs4 import BeautifulSoup

url = 'https://website-by-team-codeclash.netlify.app/academic'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

pdf_divs = soup.find_all('div', class_='col-md-4 col-sm-6 mb-3')

base_url = 'https://website-by-team-codeclash.netlify.app/academic/'

for div in pdf_divs:
    a_tag = div.find('a', href=True)
    if a_tag and a_tag['href'].endswith('.pdf'):
        pdf_url = base_url + a_tag['href'].replace('\\', '/')

        pdf_name = a_tag['download'].split('\\')[-1]

        print(f"Downloading {pdf_name}")

        pdf_response = requests.get(pdf_url)
        with open(pdf_name, 'wb') as f:
            f.write(pdf_response.content)
        print(f"Saved {pdf_name}")