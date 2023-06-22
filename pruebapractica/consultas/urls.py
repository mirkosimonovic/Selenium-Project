from django.urls import path
from .views import listar_jurisprudencias

# Nombre de la aplicación
app_name = 'consultas'

# Configuración de las rutas de URL
urlpatterns = [
    # Ruta de URL para listar las jurisprudencias
    path('jurisprudencias/', listar_jurisprudencias, name='jurisprudencias'),
]
