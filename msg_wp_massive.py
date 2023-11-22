import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Leer datos del archivo CSV
with open('numeros.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Abrir el navegador
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(30)

for row in data:
    number = row['numero']
    # user = row['usuario']

    # Primer mensaje
    message_part1 = '''Muy buenas noches, la sesion de bienvenida a los organizers ya comenzo el link es el siguiente si aun no entraste https://meet.google.com/nzo-tvxo-feu'''

    driver.get('https://web.whatsapp.com/send?phone=' + number + '&text=' + message_part1)
    time.sleep(5)

    # Esperar hasta que el botón de enviar esté visible
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-icon="send"]')))
    button.click()
    time.sleep(5)

    # # Segundo mensaje
    # message_part2 = '''Usuario: {} Contraseña: DS2023Estudiantes'''

    # driver.get('https://web.whatsapp.com/send?phone=' + number + '&text=' + message_part2.format(user))
    # time.sleep(5)

    # # Esperar hasta que el botón de enviar esté visible
    # wait = WebDriverWait(driver, 10)
    # button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-icon="send"]')))
    # button.click()
    # time.sleep(5)

    # # Tercer mensaje
    # message_part3 = '''Una vez que ingrese al link debe hacer click en "Ingresar", posteriormente ingrese el usuario y contraseña'''

    # driver.get('https://web.whatsapp.com/send?phone=' + number + '&text=' + message_part3)
    # time.sleep(5)

    # Esperar hasta que el botón de enviar esté visible
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-icon="send"]')))
    button.click()
    time.sleep(5)

# Cerrar la sesión de WhatsApp Web
more_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-icon="menu"]')))
more_button.click()
time.sleep(8)

# Dar click al botón de cerrar sesión por medio del data-testid mi-logout menu-item
logout_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li[data-testid="mi-logout menu-item"]')))
logout_button.click()
time.sleep(8)

# Dar click a aceptar en el mensaje de confirmación
logout_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="popup-controls-ok"]')))
logout_button.click()
time.sleep(8)

print('Mensajes enviados con éxito')

# Cerrar el navegador
driver.close()
