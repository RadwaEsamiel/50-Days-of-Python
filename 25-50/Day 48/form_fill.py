from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
email = driver.find_element(By.XPATH, '/html/body/form/input[3]')


first_name.send_keys("Radwa")
last_name.send_keys("Esmaiel")
email.send_keys("radwaesmaiel13@gmail.com")

submit = driver.find_element(By.XPATH, '/html/body/form/button')

submit.click()
