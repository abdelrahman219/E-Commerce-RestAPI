from django.db import models
from products.models import Product
from users.models import UserModel
# Create your models here.
class Cart(models.Model):
    total_price = models.DecimalField(null= True, blank= True)
    products = models.ManyToManyField(Product) 
    user = models.OneToOneField(UserModel , related_name = 'wishlist' , on_delete=models.CASCADE)