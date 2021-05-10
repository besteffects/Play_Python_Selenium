from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.implicitly_wait(15)
driver.get('https://esindbaad.com/')
driver.find_element_by_css_selector(".item-vertical.with-sub-menu.hover>a[href*='cat1_id=5&cat2_id=0&cat3_id=0']").click()
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products-list>.product-layout")))
cards = driver.find_elements_by_css_selector(".products-list>.product-layout")
length = len(cards)
print(length)
driver.quit()

views = driver.find_element_by_css_selector(".vcOH2>span")
print(views.text)
views.click()
likes = driver.find_element_by_css_selector(".vJRqr>span")
print(likes.text)
views.click()
exit_post = driver.find_element_by_css_selector("a[href*=explore]>svg").click()
