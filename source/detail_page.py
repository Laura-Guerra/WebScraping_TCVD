from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura el driver de Selenium
driver = webdriver.Chrome()

# Abre la URL
url = 'https://www.airbnb.es/rooms/921724642433441499?adults=2&check_in=2024-01-01&check_out=2024-01-08&source_impression_id=p3_1699384877_HSS4SI8lZpGuBDzi&previous_page_section_name=1000&federated_search_id=2ed0be9b-4cd1-42fa-87d6-4e2fbe3d8f52'
driver.get(url)

# Espera a que el elemento con la clase específica esté presente
try:
    # Espera hasta un máximo de 10 segundos antes de salir si no puede encontrar el elemento
    elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_1y74zjx"))
    )
    print("Elemento encontrado:", elemento)
    print("Contenido del elemento:", elemento.get_attribute('innerHTML'))

    # Guardar contenido en un archivo
    with open("elemento.html", "w", encoding="utf-8") as archivo:
        archivo.write(elemento.get_attribute('innerHTML'))

except Exception as e:
    print("Hubo un error al buscar el elemento:", e)

finally:
    driver.quit()
