from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response

from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from .serializers import UserSerializer
from rest_framework import status
from users.models import UserModel, UserManager
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.permissions import IsAuthenticated
from .authentication import JWTAuthentication
from .emails import send_email


# Create your views here.
@api_view(["POST"])
def register(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            subject='Welcome to E-commerce'
            message=f'Thank you {request.data.get("first_name")} for joining us, and we look forward to seeing you around the site!'
            sender ='djangocommerce@gmail.com'
            recipient_lis = [request.data.get("email")]
            #send_email(subject=subject, message=message, from_email=sender, recipient_list=recipient_lis)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
def update_user(request):
    serializer = UserSerializer(request.user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    email = request.data["email"]
    password = request.data["password"]
    user = get_object_or_404(UserModel, email=email)

    if user is None:
        raise AuthenticationFailed("User not found!")

    if not user.check_password(password):
        raise AuthenticationFailed("Incorrect password")

    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, "secret", algorithm="HS256")

    response = Response()
    response.set_cookie(key="jwt", value=token, httponly=True)
    response.data = {"jwt": token}
    return response


@api_view(["GET"])
def get_user(request):
    token = request.COOKIES.get("jwt")

    if not token:
        raise AuthenticationFailed("Unauthenticated")
    try:
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated")

    user = UserModel.objects.filter(id=payload["id"]).first()
    serialzer = UserSerializer(user)
    return Response(serialzer.data)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def hello(request):
    st = f"hello , {request.user.first_name}"
    return Response(st)


@api_view(["GET"])
def logout(request):
    response = Response()
    response.data = {"message": "Logged out successfully"}
    response.delete_cookie("jwt")
    return response


# TO DO ::: make it as a default class
