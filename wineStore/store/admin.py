from django.contrib import admin
from .models import Wine, Cart, Client, Order, WineOrder
admin.site.register((Wine,Cart,Client,Order, WineOrder))

# Register your models here.
