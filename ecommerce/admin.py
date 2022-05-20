from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(ContactUs)
# admin.site.register(Category)
admin.site.register(PaymentType)
