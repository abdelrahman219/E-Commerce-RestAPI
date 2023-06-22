from django.shortcuts import render
from django.http.response import JsonResponse
from .models import WishList,UserModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WishListSerializer
from rest_framework import status,filters
from products.serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def get_wish_list(request, id):
    wishlist = WishList.objects.filter(user__id=id).first () # Assuming the user is linked by 'user' foreign key field
    products = wishlist.products.all()
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)
