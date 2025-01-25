import requests
from bs4 import BeautifulSoup
from Emails import send_email

url = "https://appbrewery.github.io/instant_pot/"

TARGET_PRICE = 100.0

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

price_element = soup.find(name="span", class_="aok-offscreen")
product_title = soup.find(id="productTitle").get_text().strip()

price_string = price_element.text.strip()

price = float(price_string.replace('$',""))

receiver_email = "radwaesmaiel13@gmail.com"


if price < TARGET_PRICE:
    send_email(receiver_email, product_title, price, url)

