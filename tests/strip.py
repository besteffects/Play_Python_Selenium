from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get("https://testingcodeclicks.blogspot.com/2021/05/facebook.html")
fb_url = "facebook.com\n"
url = fb_url.rstrip()
locator = f"//a[contains(@href, '{url}')]"
print(type(locator))
print(type(url))
print(locator)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
driver.find_element_by_xpath(locator).click()
# driver.close()
# driver.quit()