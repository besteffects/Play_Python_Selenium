from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
start_time = time.time()
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
# prefs = {'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option("prefs", prefs)  # disable loading pictures
options.headless = True  # running in headless mode
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path='/snap/bin/chromium.chromedriver')

driver.get("https://www.nike.com.br/chuteira-nike-premier-2-sala-unissex-153-169-171-309321")
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cc-allow'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='tamanho__idM40F395']"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#anchor-acessar-unite-oauth2'))).click()
end_time = time.time()
print("Total execution time: {} seconds".format(end_time - start_time))