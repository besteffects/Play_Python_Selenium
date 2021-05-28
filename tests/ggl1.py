from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import sys
import asyncio

"""
    Chromedriver Options / Driver setting
"""
options = webdriver.ChromeOptions()
#ptions.add_argument('headless')
options.add_argument('window-size=1920,1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', chrome_options=options)

driver.get('https://ggl-maxim.com/')

driver.find_element_by_xpath("//input[@type='text']").send_keys('tnrud3080')
driver.find_element_by_xpath("//input[@type='password']").send_keys('tnrud3080')
driver.find_element_by_css_selector('.btn_apply').click()

time.sleep(2)
driver.get('https://ggl-maxim.com/api/popup/popup_menu.asp?mobile=0&lobby=EVOLUTION')
wait = WebDriverWait(driver, 20)
wait.until(EC.frame_to_be_available_and_switch_to_it("gameIframe"))
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".svg--1nrnH")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wrapper--1zUtU button>span")))
driver.find_element_by_css_selector(".wrapper--1zUtU button").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'iframe[src^="https://evo.kplaycasino.com/frontend/evo/r2/#category"]')))
iframe2 = driver.find_element_by_css_selector('iframe[src^="https://evo.kplaycasino.com/frontend/evo/r2/#category"]')
driver.switch_to.frame(iframe2)
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".svg--1nrnH")))
