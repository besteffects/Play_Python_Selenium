from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://www.tradingview.com/chart/')
wait = WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.ID, "header-toolbar-symbol-search"))).click()  # Find the search box
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-Hsmn_0WX.upperCase-Hsmn_0WX.input-3n5_2-hI"))).send_keys("VETUSD")
browser.close()