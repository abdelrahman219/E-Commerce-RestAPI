# from django.conf import settings
# from django.contrib import admin
# from wish_list import views

# from django.urls import include, path
# from cart.views import add_to_cart, get_cart
# from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from cart.views import add_to_cart, get_cart
from django.conf.urls.static import static
from wish_list.views import get_wish_list
urlpatterns = [
    path('user/', include('users.urls')),
    path("admin/", admin.site.urls),
    path('products/', include('products.urls')),
    path("api/cart/add/", add_to_cart, name="add-to-cart"),
    path("api/cart/get/", get_cart, name="get-cart"),
    # path("api/cart/delete/", checkout, name="delete-cart"),
    path('wishlist/', get_wish_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
