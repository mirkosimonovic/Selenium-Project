from django.urls import path
from .views import listar_jurisprudencias

app_name = 'consultas'
urlpatterns = [
    path('jurisprudencias/', listar_jurisprudencias, name='jurisprudencias'),
]
