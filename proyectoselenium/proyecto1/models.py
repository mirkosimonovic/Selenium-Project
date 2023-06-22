from django.db import models

class Informacion(models.Model):

    # Nuevos campos para los filtros
    region = models.CharField(max_length=100)
    gobernacion_maritima = models.CharField(max_length=100)
    capitania_puerto = models.CharField(max_length=100)

    # ...

    class Meta:
        verbose_name_plural = "Informacion"

def __str__(self):
    return f"Información: {self.region} - {self.gobernacion_maritima} - {self.capitania_puerto}"