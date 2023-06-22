from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null= True, blank= True)
    email = models.EmailField(unique=True,default='default@gmail.com')
    password = models.CharField(max_length=255,default='123')
    name = models.CharField(max_length=255,default='Name')
    
    def __str__(self):
        return self.name              # function to change name 