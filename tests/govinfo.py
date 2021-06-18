# import sys
# import time
# import re
# import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
#
# _USE_VIRTUAL_DISPLAY = False
# _FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
# # logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
# logging.basicConfig(format=_FORMAT, level=logging.INFO)
# _LOGGER = logging.getLogger(sys.argv[0])
# _DEFAULT_SLEEP = 0.5


options = options()
# options.headless = True

driver = webdriver.Firefox(options=options)

print("Started Browser and Driver")

url = 'https://www.govinfo.gov/app/collection/uscourts/district/alsd/2021/%7B%22pageSize%22%3A%22100%22%2C%22offset%22%3A%220%22%7D'

driver.get(url)

page = driver.page_source
soup = bs(page, "html.parser")
print(soup)

next_page = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='custom-paginator']//li[@class='next fw-pagination-btn']/a")))
next_page.click()

# driver.quit()