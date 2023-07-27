from django.shortcuts import render,get_object_or_404
from django.http.response import JsonResponse
from products.models import Product
from .models import WishList,UserModel
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from .serializers import WishListSerializer
from rest_framework import status,filters
from products.serializers import ProductSerializer
from users.authentication import JWTAuthentication
# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
def get_wish_list(request):
    if request.method == 'GET':
        wishlist = get_object_or_404(WishList, user=request.user)
        serializer = WishListSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        wishlist = WishList.objects.filter(user=request.user).first()
        if wishlist is None:
            wishlist = WishList(user=request.user)
            wishlist.save()

        serializer = WishListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_id = serializer.validated_data.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        wishlist.products.add(product)

        serializer = WishListSerializer(wishlist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

