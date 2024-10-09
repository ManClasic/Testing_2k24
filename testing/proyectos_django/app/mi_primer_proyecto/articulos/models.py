from django.db import models


class Articulo(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    stock = models.SmallIntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.nombre