from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

browser.get('https://www.trovaprezzi.it/televisori-lcd-plasma/prezzi-scheda-prodotto/lg_oled_cx3?sort=prezzo_totale')
wait = WebDriverWait(browser, 10)
wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".merchant_name_and_logo img")))

listings = browser.find_elements_by_css_selector(".listing_item.clearfix")

result = []
for listing in listings:
    name = listing.find_element_by_css_selector(".merchant_name_and_logo img").get_attribute("alt")
    price = listing.find_element_by_css_selector(".item_total_price").text
    result.append([name, price])

# print(*result, sep='\n')
for item in result:
  print(item[0], ', '.join(map(str, item[1:])))