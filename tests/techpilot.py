from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Set some Selenium Options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Webdriver
wd = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=options)
# URL
url = 'https://www.techpilot.de/zulieferer-suchen?laserschneiden%202d%20(laserstrahlschneiden)'

# Load URL
wd.get(url)

# Get HTML
soup = BeautifulSoup(wd.page_source, features="html.parser")

wait = WebDriverWait(wd, 15)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bodyJSP #CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))).click()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#efficientSearchIframe")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".hideFunctionalScrollbar #CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))).click()
#wd.switch_to.default_content()  # you do not need to switch to default content because iframe is closed already
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".fancyCompLabel")))

results = wd.find_elements_by_css_selector(".fancyCompLabel")

for p in results:
    print(p.text)
