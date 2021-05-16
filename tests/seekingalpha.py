from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

LOGIN_PAGE = "https://www.seekingalpha.com/login"
ACCOUNT = "Account"
PASSWORD = "Password"

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', chrome_options=chrome_options)
wait = WebDriverWait(driver, 30)
driver.get("https://www.seekingalpha.com/login")
wait.until(EC.element_to_be_clickable((By.NAME, ""))).send_keys("s")
wait.until(EC.element_to_be_clickable((By.ID, ""))).send_keys("")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in']"))).click()

driver.get("https://seekingalpha.com/article/4414043-agenus-inc-agen-ceo-garo-armen-on-q4-2020-results-earnings-call-transcript")
driver.implicitly_wait(10)
text_element = driver.find_elements_by_xpath("//*[@data-test-id='content-container']/p")

text = text_element
for t in text:
    print(t.text)