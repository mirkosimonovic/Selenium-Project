from django.apps import AppConfig

class ConsultasConfig(AppConfig):
    # Configuración del campo de autoincremento para modelos
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nombre de la aplicación
    name = 'consultas.consultas'
    
    # Nombre legible de la aplicación
    verbose_name = 'consultas'
    
    # Etiqueta de la aplicación
    label = 'consultas'

 
