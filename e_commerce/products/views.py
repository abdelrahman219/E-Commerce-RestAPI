from .models import Product
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import ProductSerializer
from users.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser


# Create your views here.
@api_view(['GET'])  
def get_products(request):
    data = {}
    try:
        products = Product.objects.all()
        search_query = request.GET.get('search', '')  
        if search_query:
            products = products.filter(name__icontains=search_query)
        products_serializer = ProductSerializer(products, many=True)
        data = products_serializer.data
        http_status = status.HTTP_200_OK   
    except Exception as e:
        print(f"Error => {e}")
        http_status = status.HTTP_404_NOT_FOUND
        
    return Response(data=data, status=http_status)

@api_view(['POST'])  
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_product(request):
    data = {}
    try:
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            data = product_serializer.data
            http_status = status.HTTP_201_CREATED
    except Exception as e:
        print(f"Error => {e}")
        http_status = status.HTTP_404_NOT_FOUND
        
    return Response(data=data, status=http_status)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_one_product(request, id):
    data = {}
    try:
        show_product = get_object_or_404(Product,id=id)
        products_serializer = ProductSerializer(show_product)
        data = products_serializer.data
        http_status = status.HTTP_200_OK
    except Exception as e:
        print("Error")
        http_status = status.HTTP_404_NOT_FOUND

    return Response(data=data, status=http_status)

@api_view(['PUT','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def edit_delete_product(request, id):
    data = {}
    try:
        show_product = get_object_or_404(Product,id=id)
        if request.method == 'PUT':
            product = ProductSerializer(instance=show_product ,data=request.data)
            if product.is_valid():
                product.save()
                data = product.data
                http_status = status.HTTP_202_ACCEPTED
        elif request.method == 'DELETE':
            show_product.delete()
            http_status = status.HTTP_200_OK
    except Exception as e:
        print("Error")
        http_status = status.HTTP_404_NOT_FOUND

    return Response(data=data, status=http_status)

