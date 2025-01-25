from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = driver.find_element(By.NAME, 'search')
search.send_keys("python")
search.send_keys(Keys.ENTER)

# driver.quit()