from django.urls import path
from .views import ejecutar_script_selenium, mostrar_informacion

urlpatterns = [
    # URL para ejecutar el script de Selenium
    path('ejecutar_script/', ejecutar_script_selenium, name='ejecutar_script'),  # Vista: ejecutar_script_selenium
    # URL para mostrar la información guardada
    path('mostrar_informacion/', mostrar_informacion, name='mostrar_informacion'),  # Vista: mostrar_informacion
]