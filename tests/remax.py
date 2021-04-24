from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
url = "https://www.remax.pt/comprar?searchQueryState={%22regionName%22:%22%22,%22businessType%22:1,%22listingClass%22:1,%22page%22:1,%22sort%22:{%22fieldToSort%22:%22ContractDate%22,%22order%22:1},%22mapIsOpen%22:false,%22listingTypes%22:[],%22prn%22:%22%22}"
driver.get(url)
wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='row results-list ']/div")))
rows = driver.find_elements_by_xpath("//div[@class='row results-list ']/div")
data = []
for row in rows:
    price = row.find_element_by_xpath(".//p[@class='listing-price']").text
    address = row.find_element_by_xpath(".//h2[@class='listing-address']").text
    price_p = row.find_element_by_xpath(".//li[@class='listing-type']").text
    area = row.find_element_by_xpath(".//li[@class='listing-area']").text
    quartos = row.find_element_by_xpath("//li[@class='listing-bedroom']").text
    data.append([price, address, price_p, area, quartos])
for p in data:
    print(p, sep='\n')


data1 = []
# for row in rows:
#     price = row.find_element_by_xpath(".//p[@class='listing-price']").text
#     address = row.find_element_by_xpath(".//h2[@class='listing-address']").text
#     type = row.find_element_by_xpath(".//li[@class='listing-type']").text
#     area = row.find_element_by_xpath(".//li[@class='listing-area']").text
#     quartos = row.find_element_by_xpath(".//i[@class='icon-bedroom-full']").text
#     data1.append(row)
# print(set(data) == set(data1))

driver.close()
driver.quit()
