from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = 'https://www.sneakql.com/en-GB/launch/culturekings/womens-air-jordan-1-high-og-court-purple-au/register'
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get(url)
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'AGREE')]"))).click()  # ACCEPT COOKIES

#  Making inputs of the first page
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#firstName"))).send_keys("test")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lastName"))).send_keys("Last name")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#preferredName"))).send_keys("Mr. President")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#email"))).send_keys("mr.president@gmail.com")
driver.find_element_by_css_selector("#password").send_keys("11111111")
driver.find_element_by_css_selector("#phone").send_keys("222334413")
driver.find_element_by_css_selector("#birthdate").send_keys("2000-06-11")
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))).click()

# Second page
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#address-autocomplete"))).send_keys("street")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#suggestion_0"))).click()




# rows= driver.find_elements_by_xpath("//strong[text()='Last matches']/ancestor::div[6]//tbody/tr")
# output = []
# for res in rows: