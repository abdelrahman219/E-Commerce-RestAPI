from rest_framework import serializers
from wish_list.models import WishList
from products.models import Product
from products.serializers import ProductSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True,many=True )
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = WishList
        fields = ('user','products',"product_id")