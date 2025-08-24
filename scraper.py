from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Configuración del navegador sin interfaz (headless)
def init_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    return driver

def login_knowlers(username, password):
    driver = init_driver()
    driver.get("https://dashboard.knowlers.app/dashboard#")

    try:
        # Aquí ajustas los selectores según la web
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Iniciar sesión')]").click()

        time.sleep(3)
        return {"message": "Login exitoso"}
    except Exception as e:
        return {"message": "Error en login", "error": str(e)}
    finally:
        driver.quit()

def search_by_dni(dni):
    driver = init_driver()
    driver.get("https://dashboard.knowlers.app/dashboard#")

    # Aquí simulas la búsqueda real por DNI
    try:
        # Ajusta los selectores correctos
        input_dni = driver.find_element(By.NAME, "dni")
        input_dni.send_keys(dni)
        driver.find_element(By.XPATH, "//button[contains(text(),'Buscar')]").click()
        time.sleep(3)

        # Simulación de resultado
        return {"dni": dni, "nombre": "Ejemplo Nombre", "resultado": "OK"}
    except Exception as e:
        return {"message": "Error en búsqueda", "error": str(e)}
    finally:
        driver.quit()

def search_by_name(nombres, apellidos):
    driver = init_driver()
    driver.get("https://dashboard.knowlers.app/dashboard#")

    try:
        # Ajusta los selectores según la web
        driver.find_element(By.NAME, "nombres").send_keys(nombres)
        driver.find_element(By.NAME, "apellidos").send_keys(apellidos)
        driver.find_element(By.XPATH, "//button[contains(text(),'Buscar')]").click()
        time.sleep(3)

        return {"nombres": nombres, "apellidos": apellidos, "resultado": "OK"}
    except Exception as e:
        return {"message": "Error en búsqueda", "error": str(e)}
    finally:
        driver.quit()
