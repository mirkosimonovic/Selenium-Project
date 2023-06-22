from django.db import models

class Informacion(models.Model):
    """
    Modelo para almacenar información con nuevos campos para los filtros.
    """

    # Nuevos campos para los filtros
    region = models.CharField(max_length=100)  # Campo de texto para la región
    gobernacion_maritima = models.CharField(max_length=100)  # Campo de texto para la gobernación marítima
    capitania_puerto = models.CharField(max_length=100)  # Campo de texto para la capitanía de puerto

    # ...

    class Meta:
        verbose_name_plural = "Informacion"  # Nombre en plural para el modelo en la interfaz administrativa

    def __str__(self):
        """
        Método para representar el objeto como una cadena de texto.
        """
        return f"Información: {self.region} - {self.gobernacion_maritima} - {self.capitania_puerto}"