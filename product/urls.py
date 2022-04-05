from django.urls import path

from product.views import *

urlpatterns = [
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name='checkout'),
]
