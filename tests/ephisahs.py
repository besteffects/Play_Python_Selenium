from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.implicitly_wait(15)
driver.get('https://ephisahs.microsoftcrmportals.com/disclaimer/restaurantinspections/edmonton-facilities/')

num = 1
facilities = []
for page in range(1, 10):
    wait = WebDriverWait(driver, 30)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//tr[@data-name]")))
    cards = driver.find_elements_by_xpath("//tr[@data-name]")

    for card in cards:
        name = card.find_element_by_xpath(".//td[@data-th='Unit Name']").text
        street1 = card.find_element_by_xpath(".//td[@data-th='Site Street 1']").text
        street2 = card.find_element_by_xpath(".//td[@data-th='Site Street 2']").text
        site_city = card.find_element_by_xpath("..//td[@data-th='Site City']").text
        province = card.find_element_by_xpath(".//td[@data-th='Site Province/State']").text
        postal_code = card.find_element_by_xpath(".//td[@data-th='Site Postal Code/Zip Code']").text
        facility_category = card.find_element_by_xpath(".//td[@data-th='Site Postal Code/Zip Code']").text
        inspections = card.find_element_by_xpath(".//td[@data-th='Inspections Completed']").text
        facilities.append([name, street1, street2, site_city, province, postal_code, facility_category, inspections])
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Next page']")))

    wait.until(EC.visibility_of_element_located((By.XPATH, "xpath=//*[contains(text(),'TEXT1') or contains(text(),'TEXT2')]")))
    driver.find_element_by_css_selector("a[aria-label='Next page']").click()
    num = num + 1
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".view-grid.has-pagination")))
    print(f"clicked page {num}")

for p in facilities:
    print(p, sep='\n')

driver.close()
driver.quit()
