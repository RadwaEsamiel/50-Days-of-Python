from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome)
driver.get("https://appbrewery.github.io/instant_pot/")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")

print(f"The price is ${price.text}")

driver.quit()