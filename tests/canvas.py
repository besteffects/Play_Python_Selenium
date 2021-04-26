import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
url = "https://play.alienworlds.io/"
driver.get(url)
driver.set_window_size(1522, 754)
time.sleep(20)
driver.implicitly_wait(25)
canvas = driver.find_element_by_css_selector("canvas[id='#canvas']")
print(driver.get_window_size())
actions = ActionChains(driver)
print("moving")
actions.move_by_offset(761, 511)
print("clicking")
actions.click()
print("clicked")
actions.perform()
print("performed")
time.sleep(10)
driver.close()
driver.quit()
