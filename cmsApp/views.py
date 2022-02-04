
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
        print(content.category)
        print(type(content.category))
        object_list = Content.objects.filter(category=content.category)
        print(object_list)
        print("Content",content)
        order_item_existed=''
        if request.user.is_authenticated :
            customer = request.user
            print("authenticate Customer:",customer)
        else:    
            device = request.COOKIES['device']
            print("device",device)
            customer, created = Customer.objects.get_or_create(device=device, username = device)
            print("device Customer:",customer)

        orders= Order.objects.filter(Q(customer = customer)& Q(status = "ordered") ).last()
        print("orders:",orders)
        if orders:
            order_item_existed = OrderItem.objects.filter(order = orders).last()
            print("order_item_existed:",order_item_existed)
        if order_item_existed :
            existed_content = Content.objects.filter(orderitem = order_item_existed)
            print("existed content",existed_content)
            if content  in   existed_content:
                context = {'object_list':object_list,'message':"this item already exist in your cart "}
                return render(request,'cmsApp/category_content_list.html',context)
        if content:
                order, created = Order.objects.get_or_create(customer = customer, status ="ordered")
                print("order",order)
                orderItem, created = OrderItem.objects.get_or_create(order=order, content=content, quantity=1)
                print("orderitem",orderItem)
                return redirect('cart')

def cart(request):
    return render(request,'cmsApp/cart.html')

          
        


    



