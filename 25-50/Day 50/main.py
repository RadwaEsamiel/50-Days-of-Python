import scraping
import form

url = f"https://appbrewery.github.io/Zillow-Clone/"
data = scraping.data_scraping(url)


for form_data in data.values() :
    form.fill_form(form_data)
    print("Data entered successfully")