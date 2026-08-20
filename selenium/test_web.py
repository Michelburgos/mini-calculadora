from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_sumar_desde_el_navegador():
    driver = webdriver.Chrome()

    try:
        driver.get("http://127.0.0.1:5000")

        campo_a = driver.find_element(By.ID, "a")
        campo_b = driver.find_element(By.ID, "b")
        selector = Select(driver.find_element(By.ID, "operacion"))
        boton = driver.find_element(By.ID, "calcular")

        campo_a.send_keys("5")
        campo_b.send_keys("3")
        selector.select_by_value("sumar")

        boton.click()

        time.sleep(1)

        assert "8.0" in driver.page_source

    finally:
        driver.quit()

# Requisitos para correr esto:
# 1) Tener la app corriendo: python app.py
# 2) Tener Chrome instalado y su chromedriver disponible en el PATH
# 3) Correr: pytest selenium/test_web.py
