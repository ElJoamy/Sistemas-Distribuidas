from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

file = open('numeros.txt', 'r')
numbers = file.readlines()
file.close()

# abrir el navegador
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(45)

texts = 'Hola que tal, buenos dias, espero que estes muy bien, paso a recordarte que el dia de hoy es nuestra charla de linkedin en el auditorio de la UPB, este ubicado en achocalla, a las 12:00 del medio dia, te esperamos :)'

for number in numbers:
    driver.get('https://web.whatsapp.com/send?phone='+number+'&text='+texts)
    time.sleep(45)
    # esperar hasta que el botón de enviar esté visible
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-icon="send"]')))
    button.click()
    time.sleep(30)

# cerrar la sesion de whatsapp web
more_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-icon="menu"]')))
more_button.click()
time.sleep(30)

# dar click al boton de cerrar sesion por medio del data-testid mi-logout menu-item
logout_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-testid="mi-logout menu-item"]')))
logout_button.click()
time.sleep(30)

# dar click a aceptar en el mensaje de confirmacion
logout_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="popup-controls-ok"]')))
logout_button.click()
time.sleep(30)

print('Mensajes enviados con exito')

# cerrar el navegador
driver.close()