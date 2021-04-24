import time
import requests
import pandas

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get(
    'https://www.remax.pt/comprar?searchQueryState={%22regionName%22:%22%22,%22businessType%22:1,%22listingClass%22:1,%22page%22:1,%22sort%22:{%22fieldToSort%22:%22ContractDate%22,%22order%22:1},%22mapIsOpen%22:false}')
driver.maximize_window()
driver.implicitly_wait(15)
wait = WebDriverWait(driver, 15)
cookies = driver.find_element_by_id('rcc-decline-button')
cookies.click()

element_list = []
for j in range(1, 2569):
    try:
        print("Searching Page " + str(j))
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='listing-search-searchdetails-component']")))
        for i in range(1, 20, 2):
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='listing-search-searchdetails-component'])[{0}]".format(i))))
            el = driver.find_element_by_xpath("(//div[@class='listing-search-searchdetails-component'])[{0}]".format(i))
            print(i)
            link = driver.find_element_by_xpath(
                "(//div[@class='listing-search-searchdetails-component'])[{0}]".format(i))
            link.click()
            try:
                detalhes = driver.find_element_by_id('details')
                preco = driver.find_element_by_id('listing-price')
                tipo = driver.find_element_by_id('listing-title')
                freguesia = driver.find_element_by_xpath('//h5[@class="listing-address"]')
                imoveis = [detalhes.text, preco.text, tipo.text, freguesia.text]
                element_list.append(imoveis)
            finally:
                driver.find_element_by_css_selector(".modal-close-icon").click()
    finally:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        next_btn = driver.find_element_by_xpath("//a[@class='page-link'][.//span[.='Next']]")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='page-link'][.//span[.='Next']]/span")))
        driver.execute_script("arguments[0].click();", next_btn)


def page_has_loaded():
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'