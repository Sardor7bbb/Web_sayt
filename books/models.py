from django.db import models

# Create your models here.


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    info = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='media/cars', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



