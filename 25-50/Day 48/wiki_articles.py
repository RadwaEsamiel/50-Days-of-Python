from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(f"The Current wikipedia article count is {count.text}")

driver.quit()