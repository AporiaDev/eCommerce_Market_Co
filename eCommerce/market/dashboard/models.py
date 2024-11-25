from django.db import models
from users.models import User

class Producto(models.Model):
    vendedor=models.ForeignKey(User,on_delete=models.CASCADE)  # Relación con el vendedor
    nombre=models.CharField(max_length=255) # Nombre del producto
    descripcion=models.TextField(blank=True,null=True)
    precio=models.DecimalField(max_digits=20,decimal_places=4)  # Precio del producto
    stock=models.PositiveIntegerField() # Cantidad en inventario
    fecha_publicacion=models.DateTimeField(auto_now_add=True) # Fecha de publicación
    imagen_url=models.URLField(max_length=1024, blank=True, null=True)
    def __str__(self):
        return self.nombre

