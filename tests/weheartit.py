from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

driver.get('https://weheartit.com/entry/349292873')
wait = WebDriverWait(driver, 15)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".panel-large.list.js-entry-panel>a>img")))
link = driver.find_element_by_css_selector(".panel-large.list.js-entry-panel>a>img").get_attribute("src")
print(link)
driver.close()
driver.quit()