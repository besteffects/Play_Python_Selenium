from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get('https://www.eneba.com/es/lego-dimensions-starter-pack-playstation-4')

wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._1FArM6>.qGNWom.qGNWom"))).click()  # accept cookies
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".EcNujK._2afX4x._1OhNBA"))).click()  # click region button
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#region .css-1hwfws3"))).click()  # change region

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#region .react-select__input>input")))
driver.find_element_by_css_selector("#region .react-select__input>input").send_keys("spa")  # input country name
driver.find_element_by_css_selector("#react-select-2-option-5").click()  # select found country
driver.find_element_by_css_selector("._3Fpvn5>button[type='submit']").click()  # submit country
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[itemprop=description]>ul>li")))  # wait for all li elements
cards = driver.find_elements_by_css_selector("div[itemprop=description]>ul>li")
for card in cards:
    print(card.get_attribute("innerHTML"))
driver.close()
driver.quit()

