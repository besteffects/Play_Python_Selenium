import time
from itertools import product
from selenium import webdriver

params = ['Parameter1', 'Parameter2', 'Parameter3', 'Parameter4']

queries = ['Query1', 'Query2', 'Query3', 'Query4',]
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

for (param, query) in product(params,queries):
    url = f'https://www.google.com/search?q=site%3A{param}+%22{query}%22'
    driver.get(url)
# driver.close()
