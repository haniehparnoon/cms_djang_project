from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.db.models import Q

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin): 
    model = CustomUser
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data["password"])
        obj.save()
    

@admin.register(Admin)
class CustomAdmin(admin.ModelAdmin):
    model = Admin
    def get_queryset(self, request):
        return Admin.objects.filter(is_superuser = True)
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data["password"])
        obj.save()    


@admin.register(Customer)
class CustomCustomer(admin.ModelAdmin):
    model = Customer
    def get_queryset(self, request):
        return Customer.objects.filter(Q(is_staff= False )and Q(is_superuser = False))
        
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data["password"])
        obj.save()    

   


  



