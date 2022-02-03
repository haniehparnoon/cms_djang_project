from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('home_admin',HomeAdmin.as_view(),name='home_admin'),
    path('home_customer',HomeCustomer.as_view(),name='home_customer'),
   
    path('home_admin/show_category/', ShowCategory.as_view(), name = 'show_category'),
]