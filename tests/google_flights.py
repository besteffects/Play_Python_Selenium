import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get('https://www.google.com/travel/flights')
assert "Google Flights" in driver.title
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".e5F5td.BGeFcf .V00Bye.ESCxub.KckZb>input[class='II2One j0Ppje zmMKJ LbIaRd']")))  # waiting for autocompleted field
field = driver.find_element_by_css_selector(".e5F5td.BGeFcf .V00Bye.ESCxub.KckZb>input[class='II2One j0Ppje zmMKJ LbIaRd']")  # finding autocompleted field
field.clear()  # clearing autocompleted field
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".BGeFcf .V00Bye.ESCxub.KckZb>input")))
click_input = driver.find_element_by_css_selector(".BGeFcf .V00Bye.ESCxub.KckZb>input")
click_input.click()  # clicking the field for a new input becoming interactible
fly_from = driver.find_element_by_css_selector("input[aria-label='Where from?']")
city = "Moscow"
fly_from.send_keys("Moscow")  # making search
# for char in city:  # when making a dynamic input
#     fly_from.send_keys(char)
#     time.sleep(0.1)