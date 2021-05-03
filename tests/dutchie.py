from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

driver.get('https://dutchie.com/embedded-menu/revolutionary-clinics-somerville/menu')

wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-card__Content-sc-7s6mw-1.cfcIOW")))
cards = driver.find_elements_by_css_selector(".product-card__Content-sc-7s6mw-1.cfcIOW")

data = []
for card in cards:
    name = card.find_element_by_css_selector(".product-information__TitleContainer-sc-65h5ke-3.fOoVwz.list-only").text
    data.append(name)
for i in data:
    print(i)
