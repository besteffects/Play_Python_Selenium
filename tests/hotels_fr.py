from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


if __name__ == "__main__":
    print("Web Scraping application started")
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1200,900")
    options.add_argument('enable-logging')

    driver = webdriver.Chrome(options=options, executable_path='/snap/bin/chromium.chromedriver')

    driver.get('https://fr.hotels.com')
    wait = WebDriverWait(driver, 15)
    try:
        element = driver.find_element_by_css_selector("#qf-0q-destination")
        if element.is_displayed():
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#qf-0q-destination")))
            destination_location_element = driver.find_element_by_css_selector("#qf-0q-destination")
            print("making input to Destination field of site 1")
            destination_location_element.send_keys('Paris, France')
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".widget-autosuggest.widget-autosuggest-visible table tr")))
            destination_location_element.send_keys(Keys.TAB)  # workaround to close destination field
            driver.find_element_by_css_selector(".widget-query-sub-title").click()
            wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".widget-query-group.widget-query-destination [aria-expanded=true]")))

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#qf-0q-localised-check-in")))
            check_in_date_element = driver.find_element_by_css_selector("#qf-0q-localised-check-in")
            check_in_date_element.send_keys(Keys.CONTROL, 'a')  # workaround to replace clear() method
            check_in_date_element.send_keys(Keys.DELETE)  # workaround to replace clear() method
            # check_in_date_element.click()
            check_in_date_element.send_keys("06/01/2021")

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#qf-0q-localised-check-out")))
            check_out_date_element = driver.find_element_by_id("qf-0q-localised-check-out")
            check_out_date_element.click()
            check_out_date_element.send_keys(Keys.CONTROL, 'a')
            check_out_date_element.send_keys(Keys.DELETE)
            check_out_date_element.send_keys("06/03/2021")
            driver.find_element_by_css_selector(".widget-query-sub-title").click()  # workaround to close end date
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#hds-marquee button"))).click()
    except:
        print("Page 1 not found")

    try:
        element = driver.find_element_by_css_selector("input[name=q-destination-srs7]")
        if element.is_displayed():
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=q-destination-srs7]")))
            destination_location_element = driver.find_element_by_css_selector("input[name=q-destination-srs7]")
            print("making input to Destination field of site 2")
            destination_location_element.send_keys('Paris, France')
            # input following data
    except:
        print("Page 2 is not found")

    try:
        element = driver.find_element_by_css_selector("form[method=GET]>div>._1yFrqc")
        if element.is_displayed():
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "form[method=GET]>div>._1yFrqc")))
            destination_location_element = driver.find_element_by_css_selector("form[method=GET]>div>._1yFrqc")
            print("making input to Destination field of site 3")
            destination_location_element.send_keys('Paris, France')
            # input following data
    except:
        print("Page 3 is not found")
