from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
# Anime = input("Enter Anime:")

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

driver.get("https://myanimelist.net/search/all?q=one%20piece&cat=all")
print(driver.title)

wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#gdpr-modal-bottom button'))).click()
search = driver.find_element_by_xpath('//input[@name="q"]')
wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="q"]')))

# Clears the field
search.send_keys(Keys.CONTROL, 'a')
search.send_keys(Keys.DELETE)

# The field is now cleared and the program can type whatever it wants
search.send_keys("anime")
search.send_keys(Keys.RETURN)
wait.until(EC.element_to_be_clickable((By.XPATH, '//h2[@id="anime"]//ancestor::div[@class="content-left"]//article[1]/div[contains(@class, "list")][1]/div[contains(@class, "information")]/a[1]')))
link = driver.find_element_by_xpath('//h2[@id="anime"]//ancestor::div[@class="content-left"]//article[1]/div[contains(@class, "list")][1]/div[contains(@class, "information")]/a[1]').click()


time.sleep(5)
