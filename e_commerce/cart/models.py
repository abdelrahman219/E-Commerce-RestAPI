from django.conf import settings
from django.db import models
from products.models import Product
# Create your models here.
class Cart(models.Model):
    total_price = models.DecimalField(null= True, blank= True, decimal_places=2 , max_digits=6)
    products = models.ManyToManyField(Product) 
    user = models.OneToOneField(settings.AUTH_USER_MODEL , related_name = 'cart' , on_delete=models.CASCADE)