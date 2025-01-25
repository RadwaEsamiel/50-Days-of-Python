from bs4 import BeautifulSoup
import requests



def data_scraping(url) :

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }

    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')


    list_items = soup.find_all("li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

    property_dict = {}
    key = 0
    for item in list_items :
        key += 1
        link_tag = item.find("a", attrs={"data-test": "property-card-link"})
        link = link_tag['href'] if link_tag else None

        price_tag = item.find("span", attrs={"data-test": "property-card-price"})
        price = price_tag.text.split('+')[0].split("/")[0].strip() if price_tag else None

        address_tag = item.find("address", attrs={"data-test": "property-card-addr"})
        address = " ".join(address_tag.text.replace("|", "").split()) if address_tag else None

        property_dict[key] = [address, price, link ]

    return property_dict