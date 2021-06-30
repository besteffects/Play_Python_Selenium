from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get("https://www.tradingview.com/markets/stocks-usa/market-movers-active/")


main = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".tv-data-table__tbody .tv-data-table__row.tv-data-table__stroke.tv-screener-table__result-row")))
companies = driver.find_elements_by_css_selector(".tv-data-table__tbody .tv-data-table__row.tv-data-table__stroke.tv-screener-table__result-row")
result = []
for company in companies:
    name_short = company.find_element_by_css_selector(".tv-screener__symbol.apply-common-tooltip").text
    name_long = company.find_element_by_css_selector(".tv-screener__description").text
    last = company.find_element_by_css_selector(".tv-data-table__cell.tv-screener-table__cell.tv-screener-table__cell--big.tv-screener-table__cell--with-marker:nth-of-type(2)>span").text
    result.append([name_short, name_long, last])
for p in result:
    print(p, sep='\n')

