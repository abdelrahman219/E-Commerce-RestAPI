from django.shortcuts import render
from django.http.response import JsonResponse
from .models import WishList,UserModel
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from .serializers import WishListSerializer
from rest_framework import status,filters
from products.serializers import ProductSerializer
from users.authentication import JWTAuthentication
# Create your views here.

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_wish_list(request):
    wishlist = WishList.objects.filter(user=request.user).first () # Assuming the user is linked by 'user' foreign key field
    products = wishlist.products.all()
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)
