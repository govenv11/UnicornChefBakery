from django.contrib import admin
from .models import Customers
from .models import Cart,Products,Productcategory
# Register your models here.

class CustomView(admin.ModelAdmin):
    list_display=['customerno','name','lastname']

admin.site.register(Customers, CustomView)
admin.site.register(Cart)
admin.site.register(Products)
admin.site.register(Productcategory)
