from django.db import models

class Jurisprudencia(models.Model):
    # Campos para almacenar la información
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    resumen = models.TextField()

    def __str__(self):
        return self.titulo
    class Meta:
        app_label = 'consultas'