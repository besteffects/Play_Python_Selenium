from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
url = 'https://library.ehaweb.org/eha/#!*menu=6*browseby=8*sortby=2*media=3*ce_id=2035*label=21986*ot_id=25553*marker=1283*featured=17286'
driver.get(url)
driver.implicitly_wait(10)
container = driver.find_elements_by_xpath("//div[contains(@class, 'test')]")
for j in container:
    link = j.find_element_by_css_selector('a').get_attribute('href')
    print(link)
driver.close()