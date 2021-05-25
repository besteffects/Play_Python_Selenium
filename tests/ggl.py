from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get('http://ggl-maxim.com/')

driver.find_element_by_xpath('//*[@id="body"]/div/div[2]/div/div[2]/fieldset/input[1]').send_keys('tnrud3080')
driver.find_element_by_xpath('//*[@id="body"]/div/div[2]/div/div[2]/fieldset/input[2]').send_keys('tnrud3080')
driver.find_element_by_xpath('//*[@id="body"]/div/div[2]/div/div[2]/fieldset/button[1]').click()

time.sleep(2)
driver.get('http://ggl-maxim.com/api/popup/popup_menu.asp?mobile=0&lobby=EVOLUTION')
wait = WebDriverWait(driver, 30)
wait.until(EC.frame_to_be_available_and_switch_to_it("gameIframe"))
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".svg--1nrnH")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-role=button-label]"))).click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sidebar-container>iframe")))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sidebar-container")))
iframe2 = driver.find_element_by_css_selector('iframe[src^="https://evo.kplaycasino.com/frontend/evo/r2/"]')
driver.switch_to.frame(iframe2)
# wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".list--BLuiJ .svg--1nrnH")))
time.sleep(20)
targets = driver.find_elements_by_css_selector(".list--BLuiJ .svg--1nrnH")
res = []
for el in targets:
    res.append(el.get_attribute('innerHTML'))
print(*res, sep='\n')

# targets = driver.find_elements_by_css_selector(".svg--1nrnH")
# res = []
# for el in targets:
#     print(len(el.get_attribute("innerHTML")))
#     res.append(el.get_attribute('innerHTML'))
# print(*res, sep='\n')