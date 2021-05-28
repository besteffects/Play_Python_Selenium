from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
driver.get('https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx')
wait = WebDriverWait(driver, 15)
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[id=divSplash]")))
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#s2id_cboTipoParticipante")))
dropdown_list = driver.find_element_by_css_selector('#s2id_cboTipoParticipante').click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-drop li:nth-child(3) div")))
option = driver.find_element_by_css_selector('#select2-drop li:nth-child(3) div')
option.click()