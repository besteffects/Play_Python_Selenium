from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')


browser.get('https://all-access.wax.io')
wait = WebDriverWait(browser, 15)
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='pannels visible-desktop-only-flex']//input[@name='userName']")))
browser.find_element_by_xpath("//div[@class='pannels visible-desktop-only-flex']//input[@name='userName']").send_keys("test")