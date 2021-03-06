import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=chrome_options)
driver.get("https://www.nike.com/login")
driver.implicitly_wait(10)
email = driver.find_element_by_xpath('//input[@type="email"]')
email.send_keys("ukr")
time.sleep(3)
password = driver.find_element_by_css_selector("input[type='password']")
password.send_keys("")
time.sleep(3)
button = driver.find_element_by_css_selector("input[type='button']")
button.click()
time.sleep(6)