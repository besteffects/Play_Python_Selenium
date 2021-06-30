from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('window-size=2560,1440')
chrome_options = Options()

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', chrome_options=options)

# Open the website page
driver.get('https://www.trivago.ie')
wait = WebDriverWait(driver, 10)

# Accept cookies
time.sleep(3)
accept_cookies = driver.find_element_by_css_selector("#onetrust-button-group>#onetrust-accept-btn-handler")
driver.execute_script("arguments[0].click();", accept_cookies)

# Enter the hotel into the search box
driver.find_element_by_id("querytext").send_keys("test hotel")

# Allow time for options to populate
time.sleep(1)

# Select the first suggestion
driver.find_elements_by_class_name("ssg-suggestion__info")[0].click()


# Allow time for the calander to pop-up
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "time[datetime='2021-07-01']")))
driver.find_element_by_css_selector("time[datetime='2021-07-11']").click()

#  Move to next date
second_date = driver.find_element_by_css_selector("time[datetime='2021-07-15']")
actions = ActionChains(driver)
actions.move_to_element(second_date)
actions.click().perform()