import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = 'my_user'
password = 'my_pass'

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/snap/bin/chromium.chromedriver')

url = "https://www.gamingintelligence.com/my-account"

driver.get(url)
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-login-tab"]')))
driver.find_element_by_xpath('//*[@id="nav-login-tab"]').click()
field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))
driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
time.sleep(10)
