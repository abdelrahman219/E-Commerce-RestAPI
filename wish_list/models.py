from django.db import models
from products.models import Product 
from users.models import UserModel
# Create your models here.
class WishList(models.Model):
    products = models.ManyToManyField(Product) 
    user = models.OneToOneField(UserModel , related_name = 'wishlist' , on_delete=models.CASCADE)