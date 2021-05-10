from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = 'https://s5.sir.sportradar.com/sports4africa/en/1/season/80526/headtohead/334075/340986/match/27195664'
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get(url)
driver.implicitly_wait(10)
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, "//strong[text()='Last matches']/ancestor::div[6]//tbody/tr")))
rows= driver.find_elements_by_xpath("//strong[text()='Last matches']/ancestor::div[6]//tbody/tr")
output = []
for res in rows:
    score = res.find_element_by_xpath(".//td[5]//div[@class=' no-wrap']").get_attribute("innerText")
    output.append(score)
print(output)
