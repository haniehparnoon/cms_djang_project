
from django.shortcuts import render,  redirect
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import *
from accounts.models import *
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

class HomePage(ListView):
    model = Category
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

class ShowContent(ListView):
    model = Content
    template_name = 'cmsApp/show_content.html'

class AddContent(CreateView):
    model = Content 
    template_name = 'cmsApp/add_content.html' 
    fields = "__all__"
    success_url = reverse_lazy('show_content')

class CategoryContentList(ListView):
    model = Content
    template_name = 'cmsApp/category_content_list.html'
     
    def get_queryset(self, *args, **kwargs):
        return Content.objects.filter(category=self.kwargs['pk'])

    def post(self, request,pk):
        content = Content.objects.get(id = pk)
        object_list = Content.objects.filter(category=content.category)
        order_item_existed=''
        if request.user.is_authenticated :
            customer = request.user
        else:    
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device, username = device)

        orders= Order.objects.filter(Q(customer = customer)& Q(status = "ordered") ).last()
        if orders:
            order_item_existed = OrderItem.objects.filter(order = orders).last()
        if order_item_existed :
            existed_content = Content.objects.filter(orderitem = order_item_existed)
            if content  in   existed_content:
                context = {'object_list':object_list,'message':"this item already exist in your cart "}
                return render(request,'cmsApp/category_content_list.html',context)
        if content:
                order, created = Order.objects.get_or_create(customer = customer, status ="ordered")
                orderItem, created = OrderItem.objects.get_or_create(order=order, content=content, quantity=1)
                return redirect('cart')

def cart(request):
    if request.user.is_authenticated :
        customer = request.user
        device = request.COOKIES['device']
        customer_device = Customer.objects.filter(device=device, username = device).last()
        order, created = Order.objects.get_or_create(customer=customer, status ="ordered")
        if customer_device:
            order_device = Order.objects.filter(customer=customer_device, status ="ordered").last()
            if order_device :
                order_items_device = OrderItem.objects.filter(order = order_device.id)
                if order_items_device:
                    Order.objects.filter(id = order.id).delete()
                    Order.objects.filter(id = order_device.id).update(customer = customer)
                    Customer.objects.filter(id = customer_device.id).delete()
                    order = Order.objects.filter(customer = customer , status = "ordered").last()
                      
    else:  
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device, username = device)
        order,created = Order.objects.get_or_create(customer=customer, status ="ordered")
    
    context = {'order':order}
    return render(request,'cmsApp/cart.html',context)


          
        


    



