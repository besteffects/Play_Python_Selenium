from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument('headless')  # start chrome without opening window

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=options)
driver.implicitly_wait(15)
listURL = [
    "https://duolingo.fandom.com/wiki/Dutch_(NL)_Skill:Basics_1",
    "https://duolingo.fandom.com/wiki/Dutch_(NL)_Skill:Basics_2",
    "https://duolingo.fandom.com/wiki/Dutch_(NL)_Skill:Phrases_1",
    "https://duolingo.fandom.com/wiki/Dutch_(NL)_Skill:Negative_1",
]


list_text = []
for url in listURL:
    driver.get(url)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[id*='google_ads_iframe']")))
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.mw-parser-output>ul>li')))
    elem = driver.find_elements_by_css_selector('.mw-parser-output>ul')
    for each_ul in elem:
        all_li = each_ul.find_elements_by_css_selector("li")
        for li in all_li:
            list_text.append(li.text)

print(list_text)
