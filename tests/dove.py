from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.implicitly_wait(10)
driver.get("https://www.dove.com/us/en/skin-care/body-lotion/cream-oil-intensive-body-lotion.html")
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "picture[class='loaded']")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".collapsed>a[title='Ingredients']")))
driver.find_element_by_css_selector(".collapsed>a[title='Ingredients']").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Go to SmartLabel')]")))
driver.find_element_by_xpath("//button[contains(text(),'Go to SmartLabel')]").click()
driver.switch_to.window(driver.window_handles[1])
driver.close()
print(driver.current_url)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)