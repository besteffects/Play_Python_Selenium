from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get('https://twitter.com/{post_author}/status/{post_id}')
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1dbjc4n.r-18u37iz.r-15zivkp .css-1dbjc4n.r-xoduu5 svg")))
driver.find_element_by_css_selector(".css-1dbjc4n.r-18u37iz.r-15zivkp .css-1dbjc4n.r-xoduu5 svg").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Report')]")))
driver.find_element_by_xpath("//span[contains(text(),'Report')]").click()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, ".r-1yadl64.r-16y2uox")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#spam-btn>div")))
spam_button = driver.find_element_by_css_selector('#spam-btn>div')
spam_button.click()



