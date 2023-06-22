from django.contrib import admin
from django.urls import path,include
from .views import get_and_add_products,one_product

urlpatterns = [
    path('', get_and_add_products),
    path('<int:id>', one_product),
]
