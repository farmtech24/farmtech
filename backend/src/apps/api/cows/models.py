from django.db import models

class Cow(models.Model):
    CATEGORY_CHOICES = [
        ('crianza', 'Crianza'),
        ('lechera', 'Lechera'),
    ]

    arete = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    nacimiento = models.DateField()
    numero_partos = models.PositiveIntegerField(default=0)
    lote = models.CharField(max_length=100)
    codigo_unico = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='productora')

    # Agregar campos adicionales
    additional_fields = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.nombre
