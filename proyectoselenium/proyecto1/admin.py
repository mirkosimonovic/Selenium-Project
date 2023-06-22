from django.contrib import admin
from .models import Informacion
@admin.register(Informacion)
class InformacionAdmin(admin.ModelAdmin):
    list_display = ('region', 'gobernacion_maritima', 'capitania_puerto')
    list_filter = ('region', 'gobernacion_maritima', 'capitania_puerto')
    search_fields = ('region', 'gobernacion_maritima', 'capitania_puerto')