
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    title = models.CharField( max_length=70)

    def __str__(self):
        return self.title

class Content(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title =  models.CharField( max_length=70)
    description = models.TextField()
    image = models.ImageField( upload_to='media/')
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Order(models.Model):
    customer = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    status_choices = [
        ("ordered","ordered"),
        ("paid","paid"),
    ] 
    status = models.CharField(choices= status_choices,default="ordered", max_length=7)

    def __str__(self):
        if self.customer.email:
            return self.customer.email+"_"+self.status
        else:
            return self.status

    @property
    def get_cart_total(self):
        orderitems = OrderItem.objects.filter(order=self.id)
        if orderitems:
            return sum([item.get_total_price for item in orderitems]) 
        else:
            return 0         


class OrderItem(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def get_total_price(self):
        content_price = Content.objects.filter(id=self.content.id).values_list("price")[0][0]
        return content_price  

class Credit(models.Model):
    cart_number = models.BigIntegerField(validators=[MinValueValidator(16)])
    price = models.IntegerField()
    password = models.IntegerField()
    date = models.DateField()
    cvv = models.IntegerField()
    customer_Credit = models.OneToOneField("accounts.Customer", on_delete=models.CASCADE)
