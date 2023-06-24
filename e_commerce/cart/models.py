from django.conf import settings
from django.db import models
from products.models import Product

# Create your models here.
# class Cart(models.Model):
#     total_price = models.DecimalField(null= True, blank= True, decimal_places=2 , max_digits=6)
#     products = models.ManyToManyField(Product)
#     user = models.OneToOneField(UserModel , related_name = 'cart' , on_delete=models.CASCADE)


class Cart(models.Model):
    total_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="cart", on_delete=models.CASCADE)

    def calculate_total_price(self):
        return sum(item.calculate_subtotal() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="carts", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def calculate_subtotal(self):
        return self.product.price * self.quantity
