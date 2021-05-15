import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def website_monitoring():
    websites = ['https://www.similarweb.com/website/zalando.de/#overview']

    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver', options=options)
    driver.get("https://www.similarweb.com/website/zalando.de/#overview")
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    time.sleep(10)

    el = driver.find_element_by_css_selector('#highcharts-0 g[zIndex="3"] .highcharts-markers.highcharts-tracker')  #  #  #highcharts-0 .highcharts-axis[zIndex="2"] path:nth-of-type(1)
    ActionChains(driver).move_to_element(el).perform()

    time.sleep(10)

    month_value = wait.until(EC.presence_of_all_elements_located((By.XPATH,
                                                                      "//*[local-name() = 'svg']/*[local-name()='g' and @class='highcharts-tooltip']/*[local-name()='text']")))


    # for crawler in websites:
    #     driver.get(crawler)
    #     wait = WebDriverWait(driver, 10)
    #
    #     website_names = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/section[1]/div[1]/div/div[1]/a').get_attribute("href")
    #     total_visits = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/span[2]/span[1]').text
    #
    #     tooltip = wait.until(EC.presence_of_element_located((By.XPATH, "//*[local-name() = 'svg']/*[local-name()='g'][8]/*[local-name()='text']")))
    #     ActionChains(driver).move_to_element(tooltip).perform()
    #     month_value = wait.until(EC.presence_of_all_elements_located((By.XPATH,
    #                                                                   "//*[local-name() = 'svg']/*[local-name()='g' and @class='highcharts-tooltip']/*[local-name()='text']")))
    #     values = [elem.text for elem in driver.find_elements_by_css_selector(".highcharts-tooltip tspan[dx]")]
    #     print('VALUES-->', values)
    #     months = driver.find_elements(By.XPATH, "//*[local-name() = 'svg']/*[local-name()='g'][6]/*/*")
    #     for date in months:
    #         print(date.text)
    #
    #     # printing all scraped data
    #     print('Website Names:', website_names)
    #     print('Total visits:', total_visits)
    # tooltip = wait.until(EC.presence_of_element_located(
    #     (By.XPATH, "//*[local-name() = 'svg']/*[local-name()='g'][8]/*[local-name()='text']")))
    #     ActionChains(driver).move_to_element(tooltip).perform()
    driver.quit()

if __name__ == "__main__":
    website_monitoring()