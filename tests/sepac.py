import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def print_hi():


    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")


    annual_pass = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=chrome_options)
    annual_pass.get("https://www.sepaq.com/en/reservation/national-parks/annual-card")

    open_eff_date_panel = annual_pass.find_element_by_link_text('Select')
    open_eff_date_panel.click()
    # wait = WebDriverWait(open_eff_date_panel, 10)
    # wait.until(EC.visibility_of_element_located(
    #     (By.CSS_SELECTOR, "//html[@class='js history es5array video opacity csspointerevents placeholder inlinesvg es5date supports es5function es5object strictmode es5string json es5syntax es5undefined es5 no-touchevents cssvhunit mediaqueries vibrate csscolumns csscolumns-width csscolumns-span csscolumns-fill csscolumns-gap csscolumns-rule csscolumns-rulecolor csscolumns-rulestyle csscolumns-rulewidth csscolumns-breakbefore csscolumns-breakafter csscolumns-breakinside flexbox csstransforms csstransforms3d no-ios panel-active']")))
    selectJuly = annual_pass.find_element_by_css_selector(
        '#reserver .panel.is-active>.panel-middle li:nth-child(3) .form-label')
    annual_pass.execute_script("arguments[0].click();", selectJuly)
    ok_button = annual_pass.find_element_by_css_selector('#reserver-date .bouton')
    ok_button.click()

    # annual_pass.close()
if __name__ == '__main__':
    print_hi() 
