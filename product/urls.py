from django.urls import path

from product.views import *

urlpatterns = [
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('delete_item/', deleteItem, name='delete_item'),
]
