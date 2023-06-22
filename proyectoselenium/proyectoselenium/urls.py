from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    # ...otras URLs del proyecto...

    # Ruta para incluir las URLs de la app 'proyecto1'
    path('proyecto1/', include('proyecto1.urls')),
]