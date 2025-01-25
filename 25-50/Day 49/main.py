import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup Chrome options
chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)
chrome.add_argument("--no-sandbox")
chrome.add_argument("--disable-dev-shm-usage")  
chrome.add_argument("--disable-extensions")  
chrome.add_argument("--disable-gpu")

# URLs
login_url = "https://www.linkedin.com/login"
job_search_url = "https://www.linkedin.com/jobs/search/?currentJobId=4080798578&distance=25.0&f_AL=true&geoId=106155005&keywords=data%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER"

driver = webdriver.Chrome(options=chrome)
wait = WebDriverWait(driver, 10)

driver.get(login_url)

try:
    email = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element(By.ID, "password")

    email.send_keys(os.getenv("LINKEDIN_EMAIL"))
    password.send_keys(os.getenv("LINKEDIN_PASSWORD"))

    signin = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    signin.click()

    wait.until(lambda d: d.current_url != login_url)
    print("Login successful!")
except Exception as e:
    print("Error during login:", e)
    driver.quit()
    exit()

driver.get(job_search_url)
print("Job search page loaded successfully!")
time.sleep(2)

try:
    easy_apply = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember54"]/span')))
    easy_apply.click()
    time.sleep(1)

    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember458"]/span')))
    next_button.click()
    time.sleep(1)

    review_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember482"]/span')))
    review_button.click()
    time.sleep(1)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember493"]/span')))
    submit.click()
    time.sleep(1)

    no_thanks = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember608"]/span')))
    no_thanks.click()

    print("Easy Apply process completed successfully!")
except Exception as e:
    print("Error during Easy Apply process:", e)
finally:
    time.sleep(5)

