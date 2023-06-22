from django.shortcuts import render
from .models import Jurisprudencia
from .utils import obtener_jurisprudencias

# Configuración de la aplicación
class Meta:
    app_label = 'consultas'

# Vista para guardar las jurisprudencias
def guardar_jurisprudencias(request):
    # Obtiene las jurisprudencias desde la API
    jurisdicciones = obtener_jurisprudencias()

    # Guarda cada jurisprudencia en la base de datos
    for jurisprudencia in jurisdicciones:
        Jurisprudencia.objects.create(
            titulo=jurisprudencia['titulo'],
            fecha=jurisprudencia['fecha'],
            resumen=jurisprudencia['resumen']
        )

    # Renderiza el template 'guardado_exitoso.html'
    return render(request, 'guardado_exitoso.html')

# Vista para listar las jurisprudencias
def listar_jurisprudencias(request):
    # Obtiene todas las jurisprudencias almacenadas en la base de datos
    jurisprudencias = Jurisprudencia.objects.all()

    # Renderiza el template 'jurisprudencias.html' y pasa las jurisprudencias como contexto
    return render(request, 'consultas/jurisprudencias.html', {'jurisprudencias': jurisprudencias})
