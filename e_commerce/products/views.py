from .models import Product
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.


@api_view(['GET','POST'])
def get_and_add_products(request):
    data = {}
    try:
        if request.method == 'GET':
            products = Product.objects.all()
            search_query = request.GET.get('search', '')  
            if search_query:
                products = products.filter(name__icontains=search_query)
            products_serializer = ProductSerializer(products, many=True)
            data = products_serializer.data
            http_status = status.HTTP_200_OK   
        elif request.method == 'POST':
            product_serializer = ProductSerializer(data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                data = product_serializer.data
                http_status = status.HTTP_201_CREATED
    except Exception as e:
        print(f"Error => {e}")
        http_status = status.HTTP_404_NOT_FOUND
        
    return Response(data=data, status=http_status)




@api_view(['GET','PUT','DELETE'])
def one_product(request, id):
    data = {}
    try:
        show_product = get_object_or_404(Product,id=id)
        if request.method == 'GET':
            products_serializer = ProductSerializer(show_product)
            data = products_serializer.data
            http_status = status.HTTP_200_OK
        elif request.method == 'PUT':
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


