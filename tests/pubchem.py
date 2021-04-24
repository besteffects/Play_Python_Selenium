import time
from selenium import webdriver

kovats = "Kovats Retention Index"
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.implicitly_wait(10)
driver.get("https://pubchem.ncbi.nlm.nih.gov/classification/#hid=72")
assert "PubChem Classification Browser" in driver.title
driver.find_element_by_xpath("//span[contains(text(), 'Chemical and Physical Properties')]").click()
driver.find_element_by_xpath("//span[contains(text(), 'Experimental Properties')]").click()
field_value = driver.find_element_by_xpath(f"//span[contains(text(), '{kovats}')]/parent::li/descendant::span[contains(@class, 'ui-button-text')][2]").text

print("Kovats Retention Index value " + field_value)

button = driver.find_element_by_xpath("//span[contains(text(), 'Kovats Retention Index')]/parent::li/descendant::span[contains(@class, 'ui-button-text')][2]").click()
time.sleep(5)
driver.close()
driver.quit()
