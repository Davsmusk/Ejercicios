from django.db import models

class Cliente(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"

