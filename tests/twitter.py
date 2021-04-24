import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')


def find_hashtags(hashtag):
    driver.get('https://twitter.com/hashtag/' + hashtag + '?src=hash')
    body = driver.find_element_by_tag_name('body')
    wait = ui.WebDriverWait(driver, 5)
    while True:
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'Icon Icon--large Icon--logo')]")))
            print("error")
            break
        except:
            body.send_keys(Keys.END)
            wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".css-901oao.r-18jsvk2.r-1qd0xha.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0>span:nth-of-type(1)")))
            tweets = driver.find_elements_by_css_selector('.css-901oao.r-18jsvk2.r-1qd0xha.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0>span:nth-of-type(1)')
            for tweet in tweets:
                print(tweet.text)


find_hashtags("any hashtag")
