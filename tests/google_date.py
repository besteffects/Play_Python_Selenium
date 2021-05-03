from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

driver.get('https://google.com/')
assert "Google" in driver.title
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gLFyf.gsfi")))
input_field = driver.find_element_by_css_selector(".gLFyf.gsfi")
input_field.send_keys("when hip-hop was born?")
input_field.send_keys(Keys.RETURN)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".Z0LcW.XcVN5d")))
result = driver.find_element_by_css_selector(".Z0LcW.XcVN5d").text
print(result)
driver.close()
driver.quit()
