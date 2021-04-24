from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import requests
import lxml.html as lh
from itertools import product

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
          "District of Columbia",
          "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
          "Maine",
          "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
          "Nevada", "New Hampshire",
          "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
          "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
          "Virginia",
          "Washington", "West Virginia", "Wisconsin", "Wyoming"]

period = "2020"

for state in states:
    driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
    driver.get('https://www.nbc.gov/pilt/counties.cfm')
    driver.implicitly_wait(20)
    state_s = driver.find_element(By.NAME, 'state_code')
    drp = Select(state_s)
    drp.select_by_visible_text(state)
    year_s = driver.find_element(By.NAME, 'fiscal_yr')
    drp = Select(year_s)
    drp.select_by_visible_text(period)
    driver.implicitly_wait(10)
    link = driver.find_element(By.NAME, 'Search')
    link.click()
    addrss = driver.current_url

    states[state].df = pd.read_html(addrss)[2]

    states[state].df['YEAR'] = period
    states[state].df['STATE'] = state

    states[state].df['PAYMENT'] = states[state].df['PAYMENT'].str.replace(r'\W', '')
    states[state].df['PAYMENT'] = states[state].df['PAYMENT'].astype(int)

    states[state].df['PAYMENT.1'] = states[state].df['PAYMENT.1'].str.replace(r'\W', '')
    states[state].df['PAYMENT.1'] = states[state].df['PAYMENT.1'].astype(int)

    states[state].df['PAYMENT.2'] = states[state].df['PAYMENT.2'].str.replace(r'\W', '')
    states[state].df['PAYMENT.2'] = states[state].df['PAYMENT.2'].astype(int)

    states[state].df['PILT/ACRE'] = states[state].df['PAYMENT'] / states[state].df['TOTAL ACRES']

# states[]