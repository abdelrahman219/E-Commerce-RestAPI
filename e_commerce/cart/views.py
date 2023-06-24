from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view , authentication_classes
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializer import CartItemSerializer, CartSerializer
from products.models import Product
from users.authentication import JWTAuthentication
from users.emails import send_email


# To Insert Item into Cart Write this in the Content box in Add to cart page
#  {
#  "product_id": 1,
#  "quantity": 2
#  }
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
def add_to_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart is None:
            cart = Cart(user = request.user)
            cart.save()
            
    try:
        cartItem_serializer = CartItemSerializer(data=request.data)
        cartItem_serializer.is_valid(raise_exception=True)

        product_id = cartItem_serializer.validated_data.get("product_id")
        quantity = cartItem_serializer.validated_data.get("quantity", 1)
        # Get the product instance
        product = get_object_or_404(Product, id=product_id)

        # Check if the product already exists in the cart
        cart_item = cart.items.filter(product=product).first()

        if cart_item:
            # Increment the quantity of the existing cart item
            cart_item.quantity += quantity
            cart_item.save()
        else:
            # Create a new cart item with the specified quantity
            cart_item = cart.items.create(product=product, quantity=quantity)

        cart.total_price = cart.calculate_total_price()
        cart.save()

        return Response(
            {"message": "Product added to cart successfully."},
            status=status.HTTP_200_OK,
        )
   
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )



@api_view(["GET" , "DELETE"])
@authentication_classes([JWTAuthentication])
def get_cart(request):
    if request.method == "GET" :
        try:
            cart = Cart.objects.get(user=request.user)

            cart_serializer = CartSerializer(cart)
            return Response(cart_serializer.data, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"error": "Cart is empty."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == "DELETE":
        try:
            cart = Cart.objects.get(user=request.user)
            total_price = cart.total_price
            cart.delete()
            
            # Send email to the user
            subject = "Cart Checkout"
            message = f"Thank you for your purchase! Total price: {total_price}"
            from_email = "muhammadjalal98@gmail.com"
            recipient_list = [request.user.email]
            
            send_email(subject, message, from_email, recipient_list)
            
            return Response({"message": "Cart deleted and email sent."}, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            return Response({"error": "Cart is empty."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# @api_view(["GET"])
# @authentication_classes([JWTAuthentication])
# def get_cart(request):
#     try:
#         cart = Cart.objects.get(user=request.user)

#         cart_serializer = CartSerializer(cart)
#         return Response(cart_serializer.data, status=status.HTTP_200_OK)

#     except Cart.DoesNotExist:
#         return Response({"error": "Cart is empty."}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# @api_view(["DELETE"])
# @authentication_classes([JWTAuthentication])
# def checkout(request):
#     try:
#         cart = Cart.objects.get(user=request.user)
#         total_price = cart.total_price
#         cart.delete()
        
#         # Send email to the user
#         subject = "Cart Checkout"
#         message = f"Thank you for your purchase! Total price: {total_price}"
#         from_email = "muhammadjalal98@gmail.com"
#         recipient_list = [request.user.email]
        
#         send_email(subject, message, from_email, recipient_list)
        
#         return Response({"message": "Cart deleted and email sent."}, status=status.HTTP_200_OK)

#     except Cart.DoesNotExist:
#         return Response({"error": "Cart is empty."}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


















# @api_view(["GET"])
# def get_cart(request):
#     try:
#         id = request.user.id
#         cart_items = CartItem.objects.filter(cart__user=id)
#         serializer = CartItemSerializer(cart_items, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(["GET"])
# def get_cart(request):
#     try:
#         cart = Cart.objects.all()
#         cart_serializer = CartItemSerializer(cart, many=True)
#         data = cart_serializer.data
#         http_status = status.HTTP_200_OK
#     except Exception as e:
#         print(f"Excption in add_to_cart => {e}")
#         http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
#     return Response(data=data, status=http_status)


# @api_view(["POST"])
# def add_to_cart(request):
#     data = {}
#     cart = get_object_or_404(Cart, id=request.user.id)
#     print(cart)
#     try:
#         cart_serializer = CartSerializer(data=request.data)
#         print(cart_serializer)
#         if cart_serializer.is_valid():
#             print(cart_serializer.is_valid)
#             cart_serializer.save()
#             data = cart_serializer.data
#             http_status = status.HTTP_200_OK
#         http_status = status.HTTP_400_BAD_REQUEST
#     except Exception as e:
#         print(f"Excption in add_to_cart => {e}")
#         data = {"error": "An error occurred"}
#         http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
#     return Response(data=data, status=http_status)
