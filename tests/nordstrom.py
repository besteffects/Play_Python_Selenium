from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=options)
driver.implicitly_wait(20)
driver.get('https://www.nordstrom.com/signin')

driver.find_element_by_name("email").send_keys("sviderskyi.vitalii@gmail.com")
wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[alt="next button"]')))
btn = driver.find_element_by_css_selector('button[alt="next button"]')
btn.click()

driver.close()
driver.quit()
