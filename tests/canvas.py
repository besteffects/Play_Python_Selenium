import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
url = "https://play.alienworlds.io/"
driver.get(url)
time.sleep(20)
driver.implicitly_wait(25)
canvas = driver.find_element_by_css_selector("canvas[id='#canvas']")
drawing = ActionChains(driver)
print("moving")
drawing.move_by_offset(450, 511)
print("clicking")
drawing.click()
print("clicked")
drawing.perform()
print("performed")
driver.close()
driver.quit()
