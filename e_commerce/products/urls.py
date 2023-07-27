from django.contrib import admin
from django.urls import path,include
from .views import get_products, add_product, get_one_product, edit_delete_product, viewsets_product
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', get_products),
    path('add', add_product),
    path('<int:id>', get_one_product),
    path('<int:id>/edit', edit_delete_product),
]
