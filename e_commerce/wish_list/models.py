from django.db import models
from products.models import Product 
from django.conf import settings
from users.models import UserModel
# Create your models here.
class WishList(models.Model):
    products = models.ManyToManyField(Product) 
    user = models.OneToOneField(settings.AUTH_USER_MODEL , related_name = 'wishlist' , on_delete=models.CASCADE)        # if usermodel(user) the WishList associated with this user will also be deleted
    
    def __str__(self):    #self hena bet reference esm el class which is WishList
        return f"Wishlist of {self.user}"
