from selenium import webdriver


class Info:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')


def get_info(self, query):
    self.query = query
    self.driver.get(url="https://www.google.com/")
    assist = info()
    assist.get_info("x")
