from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=chrome_options)
driver.get("https://www.nike.com.br/cosmic-unity-153-169-211-324680")
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cc-allow'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@for="tamanho__id40"]'))).click()
