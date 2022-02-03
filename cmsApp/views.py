from re import template
from django.shortcuts import render
from django.views.generic import TemplateView,ListView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class HomeAdmin(TemplateView):
    template_name = 'cmsApp/home_admin.html'

class HomeCustomer(TemplateView):
    template_name = 'cmsApp/home_customer.html'


