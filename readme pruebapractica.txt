Descripción
Dada la siguiente URL pública de Chile 'https://www.buscadorambiental.cl/buscador/#/jurisprudencia' desarrolle los siguiente requerimientos:

Librería requerida a utilizar: Requests
Obtenga la petición POST (list) con las jurisprudencias.
Crear una función que obtenga la información presentada en la petición.
Crear un modelo para la información presentada en la petición.
Guardar en el modelo la información obtenida.
Opcional. Generar vista en el administrador para visualizar la información obtenida.
Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.

/////////////////

Configuración del entorno:
Instala Django 4.0 y PostgreSQL en tu sistema.
Crea un nuevo proyecto Django usando el comando django-admin startproject proyecto1.
Configura la base de datos en el archivo settings.py del proyecto para utilizar PostgreSQL
Ejecuta el siguiente comando para instalar la librería Requests: 'pip install requests'
En el directorio de la aplicación Django, se abre el archivo models.py y se define un modelo para almacenar la información obtenida de la URL mencionada.
Crea un archivo utils.py en el directorio de la aplicación Django y define una función para obtener la información de la URL utilizando la librería Requests
En el archivo views.py de la aplicación Django, importa el modelo y la función definida en el paso anterior. Crea una vista o una función de vista que llame a la función obtener_jurisprudencias() 
y guarde la información obtenida en el modelo Jurisprudencia
se crea una vista al administrador para visualizar la informacion obtenida modificando admin.py
Crea un archivo de plantilla HTML, por ejemplo, jurisprudencias.html, y se utiliza Bootstrap 5 para mostrar la información del modelo Jurisprudencia obtenida desde la base de datos
