Descripción
Dada la siguiente URL pública de Chile 'https://www.concesionesmaritimas.cl/' desarrolle los siguiente requerimientos:

Librería requerida a utilizar: Selenium WebDriver
Crear un script para obtener la información presentada en una tabla luego de filtrar.
Los filtros a utilizar son los siguientes:
Región: II
Gobernación Marítima: Antofagasta
Capitanía de Puerto: Antofagasta
El script deberá recorrer todas las páginas y obtener la información de las tablas.
El script deberá crear un archivo .json con la información obtenida.
Generar modelo para guardar la información obtenida.
Opcional. Generar vista en el administrador para visualizar la información obtenida.
Opcional. Generar una vista con la información en Bootstrap 5 u otro similar.

////////////////////////////

Configuración del entorno:

Instala Django 4.0 y PostgreSQL en tu sistema.
Crea un nuevo proyecto Django usando el comando django-admin startproject proyecto1.
Configura la base de datos en el archivo settings.py del proyecto para utilizar PostgreSQL.

Configuración de Selenium:
Se Instala Selenium WebDriver utilizando pip install selenium.
Descarga el controlador de Selenium WebDriver para el navegador que deseas utilizar (por ejemplo, ChromeDriver para Google Chrome).
Configura Selenium para que use el controlador descargado en tu script.

Para obtener información de la página web:
se creo un script en Python que utilice Selenium para abrir la URL https://www.concesionesmaritimas.cl/ y realizar los filtros necesarios.
Utiliza las funciones y métodos de Selenium para interactuar con la página web, buscar elementos y extraer la información de la tabla.
Recorre todas las páginas y guarda la información obtenida en una estructura de datos (como una lista de diccionarios).

Para generar un archivo JSON con la información obtenida:

Utiliza la biblioteca integrada de Python json para guardar la información obtenida en un archivo JSON.
Serializa la estructura de datos obtenida en el paso anterior y guárdala en un archivo JSON.

Crear un modelo en Django:
Se define un modelo en Django que refleje la estructura de la información obtenida.
Se define los campos necesarios en el modelo para almacenar los datos relevantes.
Se ejecutan las migraciones necesarias para crear la tabla correspondiente en la base de datos.

para generar una vista en el administrador de Django:
Se registra el modelo creado en el archivo admin.py de tu aplicación.
Se personaliza la vista en el administrador para que muestre la información de forma adecuada.
Se genera una vista con Bootstrap:

Creamos una plantilla HTML utilizando Bootstrap o cualquier otro framework similar.
Pasamos los datos obtenidos del archivo JSON o directamente del modelo a la plantilla.
Renderizamos los datos en la plantilla HTML para mostrar la información en un formato agradable.



los pasos anteriores detallados tecnicamente:

crear un nuevo proyecto Django:

Ejecuta el comando django-admin startproject nombre_proyecto para crear un nuevo proyecto Django.
Crea una nueva aplicación Django:

Ejecuta el comando python manage.py startapp nombre_app para crear una nueva aplicación dentro del proyecto.
Configura la base de datos PostgreSQL:

En el archivo settings.py, dentro del proyecto, actualiza la configuración de la base de datos para utilizar PostgreSQL. Asegúrate de proporcionar los detalles de conexión correctos.
Define los modelos:

En el archivo models.py de la aplicación, define los modelos necesarios para almacenar la información obtenida. se puede crear un modelo llamado Informacion con los campos relevantes.
Realiza las migraciones:

Ejecuta python manage.py makemigrations para generar las migraciones basadas en los modelos definidos.
Luego, ejecuta python manage.py migrate para aplicar las migraciones y crear las tablas correspondientes en la base de datos.
Crea las vistas:

En el archivo views.py de la aplicación, define las vistas necesarias para mostrar la información obtenida. Puedes usar las vistas basadas en clase o las vistas funcionales, según tus preferencias.
Configura las URL:

En el archivo urls.py de la aplicación, define las URL necesarias para acceder a las vistas creadas.
Crea las plantillas HTML:

Crea archivos HTML en la carpeta templates de la aplicación para representar las diferentes vistas. Se Utiliza Bootstrap para dar estilo a las plantillas.
Ejecuta el script de Selenium:

para tu script de Selenium, realiza el codigo dentro de views.py. Asegúrate de importar las bibliotecas necesarias, configurar Selenium para usar el controlador adecuado y realizar las interacciones requeridas para obtener la información deseada.
Guarda la información obtenida en la base de datos:

Desde tu script de Selenium, después de obtener los datos de la página web, guarda la información en la base de datos utilizando los modelos y la API de Django ORM.