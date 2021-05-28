from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os
import datetime
from datetime import datetime
import smtplib, ssl
from random import sample


def password_generator(longitud):
    abc_minusculas = "abcdefghijklmnopqrstuvwxyz"

    abc_mayusculas = abc_minusculas.upper()

    numeros = "0123456789"

    secuencia = abc_minusculas + abc_mayusculas + numeros

    password_union = sample(secuencia, longitud)

    password_result = "".join(password_union)

    return password_result


PATH = '/snap/bin/chromium.chromedriver'
driver = webdriver.Chrome(executable_path=PATH)

driver.get("http://siga.frba.utn.edu.ar/")
print(driver.title)
wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-try"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Usuarios registrados')]"))).click()
search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='form_email']")))
search.send_keys("35335")
search.send_keys(Keys.RETURN)
