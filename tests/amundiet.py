from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


url = "https://www.amundietf.co.uk/professional/product/view/LU1681038243"
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.implicitly_wait(10).g
driver.find_element_by_xpath('//button[@data-is-focusable="true"]').click()
driver.get(url)
driver.find_element_by_id("footer_tc_privacy_button_3").click()
driver.find_element_by_id("validateDisclaimer").click()
WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fpFrame.fpBannerMore #blockleft>#part_principale_1")))
soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find_all("tr", class_="odd")
print(results)
driver.close()
driver.quit()
