from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')


def number_of_doors():
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".number .doors")))
    return driver.find_element_by_css_selector(".number .doors").text


def number_of_windows():
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".number .windows")))
    return driver.find_element_by_css_selector(".number .windows").text


if number_of_doors() == number_of_windows():
    print('Doors and windows matched')
elif number_of_doors() != number_of_windows():
    print('Doors and windows not matched')

