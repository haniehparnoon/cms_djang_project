
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class HomeAdmin(TemplateView):
    template_name = 'cmsApp/home_admin.html'

class HomeCustomer(TemplateView):
    template_name = 'cmsApp/home_customer.html'

class ShowCategory(ListView):
    model = Category
    template_name = 'cmsApp/show_category.html'

class AddCategory(CreateView):
    model = Category 
    template_name = 'cmsApp/add_category.html' 
    fields = "__all__"
    success_url = reverse_lazy('show_category')



