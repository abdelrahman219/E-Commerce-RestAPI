from django.db import models
from products.models import Product 
from django.conf import settings
# Create your models here.
class WishList(models.Model):
    products = models.ManyToManyField(Product) 
    user = models.OneToOneField(settings.AUTH_USER_MODEL , related_name = 'wishlist' , on_delete=models.CASCADE)