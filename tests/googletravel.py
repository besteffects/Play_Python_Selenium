import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.options import Options

url = 'https://www.google.com/flights?hl=en#flt=SFO.JFK.2021-06-01*JFK.SFO.2021-06-07'
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', chrome_options=chrome_options)
driver.get(url)
# wait = WebDriverWait(driver, 20)
# wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".EA71Tc.q7Eewe")))
time.sleep(10)
history = driver.find_element_by_css_selector(".EA71Tc.q7Eewe").get_attribute("innerHTML")
print(history)

driver.quit()