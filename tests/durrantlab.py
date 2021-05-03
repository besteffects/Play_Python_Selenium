from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import argparse
from pathlib import Path

#
# def dir_path(string):
#     if Path(string).exists():
#         return Path(string).resolve()
#     else:
#         raise FileNotFoundError(string)
#
#
# parser = argparse.ArgumentParser(description='Pass arguments to feed to webina.')
# parser.add_argument('--receptor', type=dir_path, required=True)
# parser.add_argument('--ligand', type=dir_path, required=True)
# parser.add_argument('--center_x', type=float, required=True)
# parser.add_argument('--center_y', type=float, required=True)
# parser.add_argument('--center_z', type=float, required=True)
# parser.add_argument('--size_x', type=float, required=True)
# parser.add_argument('--size_y', type=float, required=True)
# parser.add_argument('--size_z', type=float, required=True)
# args = parser.parse_args()

browser = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')

browser.get('https://durrantlab.pitt.edu/webina/')
browser.implicitly_wait(15)
# receptor_file = browser.find_element_by_id('__BVID__16')
# lignad_file = browser.find_element_by_id('__BVID__20')
center_x = browser.find_element_by_id('center_x')
center_y = browser.find_element_by_id('center_y')
center_z = browser.find_element_by_id('center_z')
size_x = browser.find_element_by_id('size_x')
size_y = browser.find_element_by_id('size_y')
size_z = browser.find_element_by_id('size_z')
start_webina = browser.find_element_by_xpath("//*[contains(text(), 'Start Webina')]")

# center_x.send_keys(repr(args.center_x))
# center_y.send_keys(repr(args.center_y))
# center_z.send_keys(repr(args.center_z))
# size_x.send_keys(repr(args.size_x))
# size_y.send_keys(repr(args.size_y))
# size_z.send_keys(repr(args.size_z))
# receptor_file.send_keys(str(args.receptor))
# lignad_file.send_keys(str(args.ligand))

center_x.send_keys("test")
center_y.send_keys("test")
center_z.send_keys("test")
size_x.send_keys("test")
size_y.send_keys("test")
size_z.send_keys("test")
# receptor_file.send_keys("test")
# lignad_file.send_keys("test")

start_webina.click()

WebDriverWait(browser, 10).until(
    ec.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Standard Output')]/../div/button")))
standard_download = browser.find_element_by_xpath("//*[contains(text(), 'Standard Output')]/../div/button")
standard_download.click()
pdbqt_download = browser.find_element_by_xpath("//*[contains(text(), 'Output PDBQT')]/../div/button").click()
browser.quit()
