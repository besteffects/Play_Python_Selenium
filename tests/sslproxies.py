from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
# driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sslproxies.org/")

wait = WebDriverWait(driver, 10)
length = len(driver.find_elements_by_xpath("//li[@class='paginate_button ']")) + 1
print(f"List length is: {length}")
data = []
try:
    for j in range(1, length):
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "section[id='list']")))
        try:
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#proxylisttable>tbody>tr>td")))
            rows = driver.find_elements_by_css_selector("#proxylisttable>tbody>tr")

            for row in rows:
                ip = row.find_element_by_xpath("./td[1]").text
                port = row.find_element_by_xpath("./td[2]").text
                code = row.find_element_by_xpath("./td[3]").text
                country = row.find_element_by_xpath("./td[4]").text
                anonymity = row.find_element_by_xpath("./td[5]").text
                google = row.find_element_by_xpath("./td[6]").text
                https = row.find_element_by_xpath("./td[7]").text
                last_checked = row.find_element_by_xpath("./td[8]").text
                data.append([ip, port, code, country, anonymity, google, https, last_checked])
        finally:
            print("Clicking Page " + str(j + 1))
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//li[@class='paginate_button next'][@id='proxylisttable_next']/a")))
            next_button = driver.find_element_by_xpath("//li[@class='paginate_button next'][@id='proxylisttable_next']/a")

            next_button.click()  # last page is not scraped
finally:
    print("done")

for p in data:
    print(p, sep='\n')
print(len(data))
