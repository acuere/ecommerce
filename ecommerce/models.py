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
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
    picture = models.ImageField(upload_to='images',blank=True)
    garantie = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True, default=0)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    title = models.CharField(max_length=100, default='')
    full_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    payments = models.ForeignKey(PaymentType,on_delete=models.CASCADE, blank=True, null=True, default=0)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    summary = models.TextField()

    def __str__(self):
        return self.title
 
#
class Category(models.Model):
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
