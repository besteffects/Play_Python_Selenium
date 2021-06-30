from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/snap/bin/chromium.chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.get("https://www.facebook.com/login")
wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.ID, "email")))
email = driver.find_element_by_id('email')
email.send_keys('myemail@sometest.com')
driver.find_element_by_id('pass').send_keys('MY PASSWORD')
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginbutton")))
driver.find_element_by_css_selector('#loginbutton').click()