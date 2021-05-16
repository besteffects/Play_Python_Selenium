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
    score = res.find_element_by_xpath(".//td[5]//div[@class='row flex-items-xs-middle']").get_attribute("innerText")
    output.append(score)
# print("All results:")
# print(output)

only_score = []
for res in rows:
    score = res.find_element_by_xpath(".//td[5]//div[@class=' no-wrap']").get_attribute("innerText")
    only_score.append(score)
# print("Only Score:")
# print(only_score)

first_score = []
second_score = []
for res in rows:
    first = res.find_element_by_xpath(".//td[5]//div[@class=' no-wrap']/div[1]").get_attribute("innerText")
    first_score.append(first)
    second = res.find_element_by_xpath(".//td[5]//div[@class=' no-wrap']/div[3]").get_attribute("innerText")
    second_score.append(second)
print(first_score)
print(second_score)
first_list = list(zip(first_score, second_score))
second_list = list(zip(second_score, first_score))
print(first_list)
print(second_list)



for i in range(0, len(output), 2): # swap all elements in list
    output[i], output[i+1] = output[i+1], output[i]
# print(output)