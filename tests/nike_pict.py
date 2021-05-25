from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
start_time = time.time()
options = webdriver.ChromeOptions()

prefs = {'profile.default_content_setting_values': {'images': 2}}
options.headless = True  # running in headless mode
options.add_experimental_option("prefs", prefs)  # disable loading pictures
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path='/snap/bin/chromium.chromedriver')

driver.get("https://www.nike.com.br/chuteira-nike-premier-2-sala-unissex-153-169-171-309321")
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cc-allow'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='tamanho__idM40F395']"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#anchor-acessar-unite-oauth2'))).click()
end_time = time.time()
print("Total execution time: {} seconds".format(end_time - start_time))