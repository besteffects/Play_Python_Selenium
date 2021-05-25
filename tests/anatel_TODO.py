import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class sistelBot:
    def __init__(self, freq1, freq2, band1, band2, uf, type):
        # print(freq1, freq2, band1, band2, uf, munIni, munFin, tipo)
        self.browser = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
        self.browser.delete_all_cookies()
        self.browser.maximize_window()
        self.freq1 = freq1
        self.freq2 = freq2
        self.band1 = band1
        self.band2 = band2
        self.uf = uf
        self.type = type

    def wait_for_object(self, type, string):
        return WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((type, string)))

    def wait_for_objects(self, type, string):
        return WebDriverWait(self.browser, 10).until(ec.presence_of_all_elements_located((type, string)))

    def selectByVisibleText(self, dropdown_locator, dropdown_text):
        select = Select(dropdown_locator)
        return select.select_by_visible_text(dropdown_text)

    def getData(self):
        self.browser.get("https://sistemas.anatel.gov.br/stel/Consultas/RecuperacaoFrequencias/Tela.asp")
        getBy = self.wait_for_object(By.CSS_SELECTOR, '#IndFiltro0')
        getBy.click()
        time.sleep(1)

        showBy = self.wait_for_object(By.CSS_SELECTOR, '#IndApresentacao3')
        showBy.click()
        time.sleep(1)

        FRinicial = self.wait_for_object(By.CSS_SELECTOR, '#pMedTransmissaoInicial')
        FRinicial.send_keys(self.freq1)
        time.sleep(1)
        bandIni = self.wait_for_object(By.CSS_SELECTOR, '#pIdtUnidadeTransmissao')
        bandIni.selectByVisibleText(self.band1)

        FRfinal = self.wait_for_object(By.XPATH, "//*[@id='pMedRecepcaoInicial']")
        FRfinal.send_keys(self.freq2)
        time.sleep(1)
        bandFin = self.wait_for_object(By.XPATH, "//select[@id='pIdtUnidadeRecepcao']")
        bandFin.selectByVisibleText(self.band2)

        # ufserv = self.Select(By.xpath("//*[@id='SiglaUF']"))
        # ufserv.selectByVisibleText("DF")
        # time.sleep(1)


bot = sistelBot('869,600', '890,500', 'MHz', 'MHz', 'DF', 1)
bot.getData()
