from django.urls import path
from .views import ejecutar_script_selenium, mostrar_informacion

urlpatterns = [
    path('ejecutar_script/', ejecutar_script_selenium, name='ejecutar_script'),
    path('mostrar_informacion/', mostrar_informacion, name='mostrar_informacion'),
]
