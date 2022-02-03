
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    title = models.CharField( max_length=70)

class Content(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title =  models.CharField( max_length=70)
    description = models.TextField()
    image = models.ImageField( upload_to='media/')
    price = models.IntegerField()

class Order(models.Model):
    customer = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

class OrderItem(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Credit(models.Model):
    cart_number = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(16)])
    price = models.IntegerField()
    password = models.IntegerField()
    date = models.DateField( auto_now=False, auto_now_add=False)
    cvv = models.IntegerField()
    customer_Credit = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE)
