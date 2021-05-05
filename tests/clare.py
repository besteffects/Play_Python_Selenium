import pickle
import time
from selenium import webdriver

url = 'https://sef.clareityiam.net/idp/login'
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get(url)
driver.implicitly_wait(10)
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
user = driver.find_element_by_id("clareity")
user.send_keys("user")
password = driver.find_element_by_xpath('//div[@data-ph="PASSWORD"]')
password.click()
password.send_keys("Password")
time.sleep(6)  # Added temporary so you could see that password stays
button = driver.find_element_by_id("loginbtn")
button.click()
