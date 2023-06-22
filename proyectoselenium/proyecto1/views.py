import json
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.shortcuts import render
from .models import Informacion


def ejecutar_script_selenium(request):
    # Configuración de Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome('C:\\Users\\M\\Desktop\\chromedriver_win32', options=chrome_options)
    
    try:
        # Código de Selenium
        driver.get("https://www.concesionesmaritimas.cl/")
        
        # Esperar hasta que la tabla se cargue en la página
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table#tabla_resultado"))
        )
        
        # Obtener el número total de páginas
        total_pages = int(driver.find_element(By.CSS_SELECTOR, "span.paginas").text)
        
        # Lista para almacenar los datos obtenidos
        data = []
        
        for page in range(1, total_pages + 1):
            # Obtener los datos de la página actual y agregarlos a la lista
            datos_pagina = obtener_datos_pagina(driver)
            data.extend(datos_pagina)
            
            # Ir a la siguiente página
            if page < total_pages:
                siguiente_pagina(driver)
        
        # Guardar los datos en un archivo JSON
        guardar_datos_json(data)
        
        # Cierra el navegador de Selenium
        driver.quit()
        
        # Devuelve una respuesta o realiza cualquier otra operación con los datos obtenidos
        return HttpResponse("Script de Selenium ejecutado correctamente.")
    except Exception as e:
        # Manejo de errores
        return HttpResponse(f"Error en la ejecución del script de Selenium: {str(e)}")

def obtener_datos_pagina(driver):
    # Lógica para obtener los datos de la tabla en la página actual
    # Puedes utilizar las funciones y métodos necesarios para extraer los datos de las filas y columnas de la tabla
    # y devolverlos en una estructura de datos adecuada, como una lista de diccionarios
    
    # Ejemplo de estructura de datos:
    datos_pagina = [
        {'columna1': 'valor1', 'columna2': 'valor2', 'columna3': 'valor3'},
        {'columna1': 'valor4', 'columna2': 'valor5', 'columna3': 'valor6'},
        # ...
    ]
    
    return datos_pagina

def siguiente_pagina(driver):
    # Lógica para ir a la siguiente página
    # Puedes utilizar las funciones y métodos necesarios para hacer clic en el botón o enlace que lleva a la siguiente página
    
    # Ejemplo de código:
    boton_siguiente = driver.find_element(By.CSS_SELECTOR, "a.siguiente")
    boton_siguiente.click()

def guardar_datos_json(data):
    # Guardar los datos en un archivo JSON
    with open('datos.json', 'w') as file:
        json.dump(data, file)

def mostrar_informacion(request):
    informacion_list = Informacion.objects.all()
    context = {'informacion_list': informacion_list}
    return render(request, 'informacion.html', context)

