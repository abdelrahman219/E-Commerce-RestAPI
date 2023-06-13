from django.db import models
from products.models import Product
from users.models import UserModel
# Create your models here.
class Cart(models.Model):
    total_price = models.DecimalField(null= True, blank= True, decimal_places=2 , max_digits=6)
    products = models.ManyToManyField(Product) 
    user = models.OneToOneField(UserModel , related_name = 'cart' , on_delete=models.CASCADE)