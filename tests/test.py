from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get('https://google.com')
time.sleep(10)