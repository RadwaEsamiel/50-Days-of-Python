from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

events_dict = {}

driver = webdriver.Chrome(options=chrome)
driver.get("https://www.python.org/")

all_lists = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
key = 0
for ul in all_lists:
    events = ul.find_elements(By.TAG_NAME, 'li')
    for event in events:
        datetime = event.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
        date_only = datetime.split("T")[0]
        event_name = event.find_element(By.TAG_NAME, 'a').text
        print(f"Date: {date_only}, Event: {event_name}")
        key += 1
        events_dict[key] = {"date" : date_only , "name" : event_name }

print(events_dict)
driver.quit()