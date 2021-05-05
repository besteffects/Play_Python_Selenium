import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.implicitly_wait(10)
driver.get('https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data/leaderboard')

wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sc-pAyMl.dwWbEz .sc-AxiKw.kOAUSS>.sc-AxhCb.gsXzyw")))
cookies = driver.find_element_by_css_selector(".sc-pAyMl.dwWbEz .sc-AxiKw.kOAUSS>.sc-AxhCb.gsXzyw").click()
load_more = driver.find_element_by_css_selector(".competition-leaderboard__load-more-count").click()
time.sleep(10)
# driver.close()
# driver.quit()
