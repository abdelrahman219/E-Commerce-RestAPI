from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False)
    description = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.name}"
