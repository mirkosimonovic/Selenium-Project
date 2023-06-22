from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('consultas/', include('consultas.urls')),
]