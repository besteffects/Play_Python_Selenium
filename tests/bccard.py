import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

options = Options()
#  Add user agent
# options.add_argument('user-agent=')
driver = webdriver.Chrome(chrome_options=options, executable_path='/snap/bin/chromium.chromedriver')
driver.get('https://www.bccard.com/app/merchant/Login.do')
driver.implicitly_wait(10)

driver.find_elements_by_css_selector("li[id^=ProgramCategoriesAndCodes_chzn]")

wait = WebDriverWait(driver, 10)
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
assert "INISAFE CrossWebEX" in alert.text
alert.dismiss()

driver.find_element_by_css_selector('li>#userid').send_keys('id')
field = driver.find_element_by_css_selector('span>#passwd')
driver.execute_script(f"arguments[0].value='pw'", field)


time.sleep(10)
