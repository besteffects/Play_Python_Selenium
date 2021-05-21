from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get("https://osu.ppy.sh/beatmapsets?m=0")
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".beatmapsets__items-row:nth-of-type(1)>.beatmapsets__item:nth-of-type(1)")))
games = driver.find_element_by_css_selector(".beatmapsets__items-row:nth-of-type(1) .beatmapsets__item:nth-of-type(1) .beatmapset-panel__info-row--extra")
actions = ActionChains(driver)
actions.move_to_element(games).perform()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".beatmaps-popup__group")))
levels = driver.find_elements_by_css_selector(".beatmaps-popup__group .beatmaps-popup-item__col.beatmaps-popup-item__col--name.u-ellipsis-overflow")
for level in levels:
    print(level.text)

scores= driver.find_elements_by_css_selector(".beatmaps-popup__group .beatmaps-popup-item__col.beatmaps-popup-item__col--difficulty")
for score in scores:
    print(score.text)