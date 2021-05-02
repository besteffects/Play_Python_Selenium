from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.implicitly_wait(10)
driver.get('https://ephisahs.microsoftcrmportals.com/disclaimer/restaurantinspections/edmonton-facilities/')

wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//tr[@data-name]")))
cards = driver.find_elements_by_xpath("//tr[@data-name]")
facilities = []
for card in cards:
    name = card.find_element_by_xpath(".//td[@data-attribute='name']").get_attribute("data-value")
    street1 = card.find_element_by_xpath(".//td[@data-attribute='address1_line1']").get_attribute("data-value")
    street2 = card.find_element_by_xpath(".//td[@data-th='Site Street 2']").text
    site_city = card.find_element_by_xpath(".//td[@data-attribute='address1_city']").text
    province = card.find_element_by_xpath(".//td[@data-attribute='address1_stateorprovince']").text
    postal_code = card.find_element_by_xpath(".//td[@data-th='Site Postal Code/Zip Code']").text
    facility_category = card.find_element_by_xpath(".//td[@data-attribute='fs_facilitycategory']").text
    inspections = card.find_element_by_xpath(".//td[@data-th='Inspections Completed']").text
    facilities.append([name, street1, street2, site_city, province, postal_code, facility_category, inspections])

for p in facilities:
    print(p, sep='\n')

driver.close()
driver.quit()
