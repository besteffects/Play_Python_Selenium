from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

driver.get(
    "https://oldnavy.gapcanada.ca/browse/product.do?pid=647076053&cid=1180630&pcid=26190&vid=1&nav=meganav%3AWomen%3ADeals%3ASale&grid=pds_0_1034_1#pdp-page-content")
driver.execute_script("window.scrollTo(0, 1000)")

wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.promoDrawer__handlebar__icon"))).click()
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".pr-rd-description-text")))
review = driver.find_elements_by_css_selector(".pr-rd-description-text")
for post in review:
    print(post.text)

# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pr-rd-pagination-btn"))).click()
element = driver.find_element_by_css_selector(".pr-rd-pagination-btn")

# actions = ActionChains(driver)
# actions.move_to_element(element).click().perform()
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)
print("clicked next")
# review2 = driver.find_elements_by_class_name("pr-rd-description-text")
# for post in review2:
#     print(post.text)