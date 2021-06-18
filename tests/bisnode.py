import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = 'https://www.bisnode.de/upik/'
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get(url)
wait = WebDriverWait(driver, 15)
link = driver.find_element_by_css_selector(".productcarousel__mainitem.slick-slide.slick-current.slick-active img").get_attribute("src")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[style='bottom: 1rem'] button[id*='onetrust-accept-btn-handler']")))
driver.find_element_by_css_selector("div[style='bottom: 1rem'] button[id*='onetrust-accept-btn-handler']").click()
time.sleep(10)
driver.quit()