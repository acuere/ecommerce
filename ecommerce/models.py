from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0)
    reduced = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images', default=True)
    garantie = models.IntegerField(default=0)

    def __str__(self):
        return self.name
