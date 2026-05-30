from django.db import models

class LeccionAprendida(models.Model):
    CATEGORIAS = [
        ('POS', 'Sistemas POS'),
        ('RED', 'Redes y Conectividad'),
        ('HW', 'Hardware y Mantenimiento'),
        ('SW', 'Software y Actualizaciones'),
        ('BD', 'Bases de Datos'),
        ('SEG', 'Seguridad Informática'),
    ]
    
    titulo = models.CharField('Título', max_length=200)
    categoria = models.CharField('Categoría', max_length=3, choices=CATEGORIAS)
    problema = models.TextField('Problema identificado')
    causa = models.TextField('Causa del problema')
    solucion = models.TextField('Solución aplicada')
    resultado = models.TextField('Resultado obtenido')
    responsable = models.CharField('Responsable', max_length=100)
    fecha_creacion = models.DateTimeField('Fecha de registro', auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Lección Aprendida'
        verbose_name_plural = 'Lecciones Aprendidas'


class Experto(models.Model):
    nombre = models.CharField('Nombre completo', max_length=100)
    area = models.CharField('Área de especialidad', max_length=100)
    expertise = models.TextField('Expertise / Conocimiento especializado')
    email = models.EmailField('Correo electrónico')
    antiguedad = models.IntegerField('Años de experiencia')
    disponible = models.BooleanField('Disponible para consulta', default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Experto'
        verbose_name_plural = 'Expertos'