
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome = webdriver.ChromeOptions()

chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)
driver.get("https://orteil.dashnet.org/cookieclicker/")

langSelect = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "langSelect-EN")))
langSelect.click()
time.sleep(2)
cookie = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="bigCookie"]')))
cookie.click()

start_time = time.time()
end_time = start_time+ 60 * 5
last_check_time = time.time()

while True:
    cookie.click()
    time.sleep(0.1)
    if time.time() - last_check_time > 10:
        max_price_product = ""
        products = driver.find_elements(By.CLASS_NAME, "product")
        upgrades = driver.find_elements(By.CLASS_NAME, "upgrades")
        enabled_products = {}

        try:
            banner = driver.find_element(By.XPATH, "/html/body/div[1]/div")
            if banner.is_displayed():
                close_button = banner.find_element(By.XPATH, "/html/body/div[1]/div/a[1]")
                close_button.click()
                time.sleep(1)
        except Exception as e:
            print("Banner not found or already closed:", e)

        for upgrade in upgrades:
            if "enabled" in upgrade.get_attribute("class"):
                upgrade_id = upgrade.get_attribute("id")

                upgrade_to_click = driver.find_element(By.XPATH,f'//*[@id="{upgrade_id}"]')
                upgrade_to_click.click()

        for product in products:
            if "enabled" in product.get_attribute("class"):
                product_id = product.get_attribute("id")
                price = product.find_element(By.CLASS_NAME, "price").text
                enabled_products[product_id] = int(price)


        max_price_product = max(enabled_products, key=enabled_products.get)
        print(f"Clicking product: {max_price_product}")

        product_to_click = driver.find_element(By.XPATH,f'//*[@id="{max_price_product}"]')
        product_to_click.click()



        last_check_time = time.time()

    if time.time() > end_time:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

