from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def fill_form(list_of_answers) :

    chrome = webdriver.ChromeOptions()
    chrome.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome)
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScyhtbe6Eoc2Nsm0VJ5IlVq27LR3WER4A2hXage-uIBi4mIIQ/viewform?usp=sf_link")

    wait = WebDriverWait(driver, 10)  # 10 seconds timeout
    q1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    q2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    q3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))


    q1.send_keys(list_of_answers[0])
    q2.send_keys(list_of_answers[1])
    q3.send_keys(list_of_answers[2])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    submit.click()

    driver.quit()