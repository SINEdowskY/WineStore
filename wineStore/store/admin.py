from django.contrib import admin
from .models import Wine, Cart, Client, Order
admin.site.register((Wine,Cart,Client,Order))

# Register your models here.
