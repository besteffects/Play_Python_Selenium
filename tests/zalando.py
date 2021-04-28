import time
import pandas
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

delay = 15

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.implicitly_wait(10)

driver.get("https://en.zalando.de/women/?q=michael+michael+kors+taschen")
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="uc-btn-accept-banner"]')))
driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()
time.sleep(10)