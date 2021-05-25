from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter
from datetime import datetime
import time
from selenium.common.exceptions import TimeoutException


trade_date_lim = "5/1/2021"

browser = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')


#makes workbook to write to
workbook = xlsxwriter.Workbook('reit_bonds_test.xlsx')
worksheet = workbook.add_worksheet()


stocks = ["PNW", "STWD"]

for stock in stocks:
    browser.get('https://finra-markets.morningstar.com/BondCenter/Default.jsp')
    wait = WebDriverWait(browser, 10)
    #using clicks and send_keys, gets the bond page for a desired stock
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           '#TabContainer > div > div.rtq-tab-wrap > div.rtq-tab-menus-wrap > ul > li:nth-child(3) > a > span'))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#firscreener-cusip'))).send_keys(stock)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                           "#ms-finra-advanced-search-form > div.ms-finra-advanced-search-btn > input:nth-child(2)"))).click()
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ms-agreement > input"))).click()
    except TimeoutException:
        pass

    #clicks to sort by earliest date, clicks again to sort by latest maturity
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-grid-hd > div > div:nth-child(7) > div"))).click()
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-grid-hd > div > div:nth-child(7) > div"))).click()
    time.sleep(5)
    #gathers all bond offerings on first page
    whole_chart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-scrollpanel > div.rtq-grid-scroll"))).text

    #gets number of bonds listed on page so we can iterate through them. Some pages have differing number of bonds listed. Most on page is 20
    parent = browser.find_element_by_xpath('//*[@id="ms-finra-search-results"]/div/div[3]/div[1]/div[1]/div[2]/div[2]/div')
    count_divs = len(parent.find_elements_by_xpath("./div"))

    bnd_off_cnt = 1
    row_num = 0
    while row_num < count_divs and bnd_off_cnt < 3:

        #gets values that I'm looking for
        symbol = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-scrollpanel > div.rtq-grid-scroll > div > div:nth-child(" + str(row_num + 1) + ") > div:nth-child(3)"))).text
        maturity = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-scrollpanel > div.rtq-grid-scroll > div > div:nth-child(" + str(row_num + 1) + ") > div:nth-child(7)"))).text
        moody_rating = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-scrollpanel > div.rtq-grid-scroll > div > div:nth-child(" + str(row_num + 1) + ") > div:nth-child(8)"))).text
        sandp_rating = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-scrollpanel > div.rtq-grid-scroll > div > div:nth-child(" + str(row_num + 1) + ") > div:nth-child(9)"))).text
        stated_bond_yield = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-scrollpanel > div.rtq-grid-scroll > div > div:nth-child(" + str(row_num + 1) + ") > div:nth-child(11)"))).text

        #looks to see if all values are non-empty and if moody rating and sandp rating are not equal to 'WR' and 'NR'
        if symbol.strip() and maturity.strip() and moody_rating.strip() and sandp_rating.strip() and stated_bond_yield.strip() and moody_rating != "WR" and sandp_rating != "NR":
            #bond detail page below
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ms-finra-search-results > div > div.qs-resultData > div.qs-resultData-body > div.rtq-grid.rtq-grid-auto-h > div.rtq-scrollpanel > div.rtq-grid-scroll > div > div:nth-child(" + str(row_num + 1) + ") > div:nth-child(2) > div > a")))
            element_link = element.get_attribute('href') #gets the link

            #opens window, switches to it and opens the bond detail page
            browser.execute_script("window.open('');")
            time.sleep(3)
            browser.switch_to.window(browser.window_handles[1])
            browser.get(element_link)

            #switch to iframe on second page and clicks it
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ms-bond-detail-iframe")))
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#tradeHistory_link"))).click()
            #switches to third page
            browser.switch_to.window(browser.window_handles[-1])
            #sleeps for 3 seconds so we know for sure that we are working on right page
            time.sleep(3)


            # get length of table on trades page and iterate through them trying to find the most recent "Trade" status
            bond_trades = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#ms-glossary > div > table > tbody > tr")))
            count = len(bond_trades)


            for trade in range(count):

                bond_trade_status = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ms-glossary > div > table > tbody > tr:nth-child(" + str(trade + 1) + ") > td:nth-child(4) > div"))).text
                if bond_trade_status == "Trade":
                    bond_last_traded = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ms-glossary > div > table > tbody > tr:nth-child(" + str(trade + 1) + ") > td:nth-child(1) > div"))).text
                    if bond_last_traded > trade_date_lim:
                        #prior bond yields occasionally don't match the yield that it was last traded at
                        bond_yield = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#ms-glossary > div > table > tbody > tr:nth-child(" + str(trade + 1) + ") > td:nth-child(7) > div"))).text
                        print(symbol, maturity, bond_yield)
                        bnd_off_cnt += 1
                        break
                    else:
                        continue
                    #test for if we are within X amount of time from today
                    #continue if we are more than that amount of time
                    #exit if we are within time frame and get 'Yield'
                else:
                    continue
        browser.switch_to.window(browser.window_handles[1])
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        row_num += 1