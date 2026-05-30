from django.contrib import admin
from .models import LeccionAprendida, Experto

@admin.register(LeccionAprendida)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'responsable', 'fecha_creacion')
    list_filter = ('categoria', 'fecha_creacion')
    search_fields = ('titulo', 'problema', 'solucion')
    fieldsets = (
        ('Identificación', {'fields': ('titulo', 'categoria')}),
        ('Contenido de la Lección', {'fields': ('problema', 'causa', 'solucion', 'resultado')}),
        ('Responsable', {'fields': ('responsable',)}),
    )

@admin.register(Experto)
class ExpertoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'area', 'email', 'antiguedad', 'disponible')
    list_filter = ('area', 'disponible')
    search_fields = ('nombre', 'area', 'expertise')