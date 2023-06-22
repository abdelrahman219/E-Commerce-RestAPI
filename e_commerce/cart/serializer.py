from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product
from products.serializers import ProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ("id", "product", "product_id", "quantity")


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True, source="items")

    class Meta:
        model = Cart
        fields = ("user", "total_price", "cart_items")


# class CartSerializer(serializers.ModelSerializer):
#     products = ProductSerializer(many=True, read_only=True)

#     # products_id = serializers.ListField(
#     #     child=serializers.IntegerField(), write_only=True
#     # )

#     class Meta:
#         model = Cart
#         fields = ("id", "total_price", "products", "products_id", "user")
