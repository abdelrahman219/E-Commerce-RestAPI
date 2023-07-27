from django.contrib import admin
from .models import UserModel
# Register your models here.
from users.models import UserModel

admin.site.register(UserModel)
