from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get("https://iasi.inoras.ro/evenimente/")
assert "Oras" in driver.title
wait = WebDriverWait(driver, 20)
cal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".eventon_daily_in")))
driver.execute_script("arguments[0].scrollIntoView();", cal)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p[data-date='20']"))).click()
events = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".eventon_list_event.evo_eventtop.dayevent")))
names = []
for event in events:
    name = event.find_element_by_css_selector(" .evcal_desc2.evcal_event_title").text
    names.append(name)
print(*names, sep='\n')
driver.close()
driver.quit()
