from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
browser.implicitly_wait(10)
browser.get("https://medium.com/search")
browser.find_element_by_xpath("//input[@type='search']").send_keys("international development", Keys.ENTER)

article_2016_t_xpath = '//div[contains(@class,"postArticle--short")][.//time[contains(@datetime, "2016")]][//span[@class="readingTime"]]'
article_element_list_t_1 = browser.find_elements_by_xpath(article_2016_t_xpath)

lista = []
timelines = []
wait = WebDriverWait(browser, 20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.readingTime')))
for article in article_element_list_t_1:
    readingtime = article.find_element_by_xpath(".//span[contains(@class, 'readingTime')]").get_attribute("title")
    Timelines = article.find_element_by_xpath(".//time").text
    timelines.append(Timelines)
    lista.append(readingtime)

for i in lista:
    print(i)
for i in timelines:
    print(i)

browser.close()
browser.quit()
