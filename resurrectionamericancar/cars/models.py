from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cars(models.Model):
    marca = models.CharField(max_length=100,default="ACURA")  # Audi, bmv,mercedes    
    body_style = models.CharField(max_length=100,default="SUV")  # truck, seddan, convertible 
    fuel_type=  models.CharField(max_length=100,default="Gasolina")#hybrid or electric
    nuevo_usado = models.CharField( max_length=100,default="usado")#new o used
    year = models.IntegerField()  # Año de fabricación
    modelo = models.CharField( default='-',max_length=100)    
    only_oneowner = models.BooleanField(default=True)
    # slug = models.SlugField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(default='fallback.png',blank=True)
    color = models.CharField( max_length=100)   
    descripcion = models.CharField( max_length=100, default='-') 
    precio = models.IntegerField(default=2000)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    en_stock = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.year})"
 