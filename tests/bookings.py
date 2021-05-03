from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = 'https://bookings.guoman.com/100259?datein=06/05/2021&dateout=06/08/2021&rooms=1&adults=1&languageid=1#/accommodation/room'
driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get(url)
#driver.implicitly_wait(10)
WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".CardList-summary-title.ng-binding")))
results= driver.find_elements_by_css_selector(".CardList-summary-title.ng-binding")
for res in results:
    print(res.text)
driver.close()
driver.quit()
