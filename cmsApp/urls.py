from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('home_admin/',HomeAdmin.as_view(),name='home_admin'),
    path('home_customer',HomeCustomer.as_view(),name='home_customer'),
    path('home_admin/show_category/', ShowCategory.as_view(), name = 'show_category'),
    path('home_admin/show_category/add_category/',AddCategory.as_view(),name = "add_category"),
    path('home_admin/show_content/', ShowContent.as_view(), name = 'show_content'),
    path('home_admin/show_content/add_content/',AddContent.as_view(),name = "add_content"),
    path('category_content_list/<int:pk>',CategoryContentList.as_view(),name = "category_content_list"),
    path('cart/',cart,name="cart"),
    path("create_credit/",CreateCredit.as_view(),name = "create_credit"),
    path("cart/orderitem_delete/<int:pk>/",OrderItemDelete.as_view(),name = "orderitem_delete"),
]