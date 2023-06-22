from django.shortcuts import render
from .models import Jurisprudencia
from .utils import obtener_jurisprudencias
class Meta:
    app_label = 'consultas'
def guardar_jurisprudencias(request):
    jurisdicciones = obtener_jurisprudencias()
    for jurisprudencia in jurisdicciones:
        Jurisprudencia.objects.create(
            titulo=jurisprudencia['titulo'],
            fecha=jurisprudencia['fecha'],
            resumen=jurisprudencia['resumen']
        )
    return render(request, 'guardado_exitoso.html')
def listar_jurisprudencias(request):
    jurisprudencias = Jurisprudencia.objects.all()
    return render(request, 'consultas/jurisprudencias.html', {'jurisprudencias': jurisprudencias})
