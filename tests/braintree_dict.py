from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
from dateutil import parser
import requests
import json

url = 'https://www.braintree.gov.uk/bins-waste-recycling/route-3-collection-dates/1'

browser = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
browser.get(url)


html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, "html.parser")

data = soup.find_all("div", {"class":"date_display"})

result = {}

for item in data:
    bin_colour = item.find('h3').text
    bin_date = parser.parse(item.find('p').text).strftime('%Y-%m-%d')
    result[bin_colour]=bin_date

#print(result)
print(json.dumps(result))

# for k, v in result.items():
#     print(k, v)
# browser.quit()