import imp
from django.contrib import admin
from .models import Category, Content, Order, OrderItem, Credit
# Register your models here.
admin.site.register(Category)
admin.site.register(Content)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Credit)
