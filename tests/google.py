from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class SiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

    def test(self):
        driver = self.driver
        driver.get('https://google.com/')
        driver.get("https://www.google.com/")
        assert "Google" in driver.title
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gLFyf.gsfi")))
        input_field = driver.find_element_by_css_selector(".gLFyf.gsfi")
        input_field.send_keys("Why are people so mad?")
        input_field.send_keys(Keys.RETURN)

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".yuRUbf")))
        results = driver.find_elements_by_css_selector(".yuRUbf>a>h3")
        for result in results:
            print(result.text)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
