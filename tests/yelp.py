from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get('https://www.yelp.com/biz/gordon-ramsay-hells-kitchen-las-vegas-3?osq=Restaurants&sort_by=date_desc')
wait = WebDriverWait(driver, 15)
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".review__373c0__13kpL.border-color--default__373c0__2oFDT")))
cards = driver.find_elements_by_css_selector(".review__373c0__13kpL.border-color--default__373c0__2oFDT")
reviews = []
for card in cards:
    date = card.find_element_by_css_selector(".margin-t1__373c0__oLmO6.margin-b1-5__373c0__2Wblx.border-color--default__373c0__2oFDT").text
    feedback = card.find_element_by_css_selector(".margin-b2__373c0__abANL.border-color--default__373c0__2oFDT>p>span").text
    reviews.append([date, feedback])
for i in reviews:
    print(i)

