import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'

options = FirefoxOptions()
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument("--headless")
options.add_argument('window-size=1920x1080')
driver = webdriver.Firefox(options=options)
start_url = "https://ammoseek.com/ammo/300aac-blackout?pl=no&co=new&ca=brass" #works with US IP
driver.get(start_url)

time.sleep(5)
text = driver.find_element_by_class_name('results-card').text
print (text)