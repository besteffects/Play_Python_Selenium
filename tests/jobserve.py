import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

driver.get('https://www.jobserve.com/gb/en/JobSearch.aspx?shid=415E7EF3D52E66613550')
wait = WebDriverWait(driver, 20)
jobs = driver.find_elements_by_css_selector(".jobsum")
data = driver.find_element_by_id("td_jobpositionlink")
print(data.text)
if "Data Scientist" in data.text:
    driver.find_element_by_link_text("Apply").click()
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#appFrame")))
    email = driver.find_element_by_css_selector(".questionblock2>.questionInput>input")
    email.send_keys("test")
    #  continue filling in fields

driver.close()
driver.quit()
