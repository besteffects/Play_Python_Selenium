import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = FirefoxOptions()
options.add_argument('window-size=1920x1080')
driver = webdriver.Firefox(options=options)
uq = "https://my.uq.edu.au/programs-courses/requirements/program/2451/2021"
driver.get(uq)
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Theory of Computing']>span:nth-of-type(1)")))
group = driver.find_element_by_css_selector("a[title='Theory of Computing']>span:nth-of-type(1)").get_attribute("innerHTML")
print(group)
