from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get("https://www.walmart.com/browse/snacks-cookies-chips/cookies/976759_976787_1001391")
assert "Walmart.com" in driver.title
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-title-link.line-clamp.line-clamp-2.truncate-title>span")))

elems = driver.find_elements_by_css_selector(".product-title-link.line-clamp.line-clamp-2.truncate-title>span")
for el in elems:
    print(el.text)
driver.close()
