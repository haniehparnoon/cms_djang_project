from django.contrib import admin
from .models import CustomUser,Customer,Admin

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Customer)
