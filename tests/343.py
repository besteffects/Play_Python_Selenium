import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#Chrome browser version 91.0.4472.77
# Crome-Driver version used: 91.0.4472.19 <--latest

url='https://www.google.co.in'
driver_path='F:\Path\chromedriver_win32\chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=chrome_options)
driver.get(url)