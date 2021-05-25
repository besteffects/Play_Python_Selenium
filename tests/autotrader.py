import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=chrome_options)

driver.maximize_window()
url = "https://www.autotrader.com/model-information"
driver.get(url)
wait = WebDriverWait(driver, 15)

makelist = []
modellist = []
#### First work with the drop down menus with car makes

make_dd = driver.find_element_by_xpath('//*[@id="makeCode"]')
model_dd = driver.find_element_by_xpath('//*[@id="ModelCode"]')
makes = driver.find_elements_by_xpath('//*[@id="makeCode"]/optgroup[@label="All Makes"]/option')
models = driver.find_elements_by_xpath('//*[@id="ModelCode"]/optgroup[2]/option')

#### Loop through all makes in the drop down menus
# for i in range(len(makes)):
#     n = 1

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="makeCode"]')))
make_dd.click()


wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="makeCode"]/optgroup[1]/option[{1}]')))
make = driver.find_element_by_xpath(f'//*[@id="makeCode"]/optgroup[1]/option[1]')
make.click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ModelCode>optgroup[Label='All Models']")))
model_dd.click()
