from django.contrib import admin
from django.urls import include, path

# Configuración de las rutas de URL
urlpatterns = [
    # Incluye las URLs de la app 'consultas'
    path('consultas/', include('consultas.urls')),
]
