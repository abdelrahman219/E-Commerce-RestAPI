from django.urls import path
from .views import get_user, register, login, hello, logout, update_user


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", register),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", login),
    path("getuser/", get_user),
    path("hello/", hello),
    path("logout/", logout),
    path("update/", update_user),
]
