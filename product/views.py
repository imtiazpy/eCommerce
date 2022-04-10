from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json

from product.models import Product, Customer, Order, OrderItem, ShippingAddress


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        cartTotal = order.get_cart_total
    else:
        items = []
        order = {'id': 0}
        cartItems = order['get_cart_items']
        cartTotal = order['get_cart_total']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'cartTotal': cartTotal
    }

    return render(request, 'product/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        cartTotal = order.get_cart_total
    else:
        items = []
        order = {'id': 0}
        cartItems = order['get_cart_items']
        cartTotal = order['get_cart_total']
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'cartTotal': cartTotal
    }

    return render(request, 'product/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    value = data['value']
    size = data['size']
    color = data['color']
    qty = data['qty']

    customer = request.user.customer
    product = get_object_or_404(Product, id=productId)

    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.size = size
        orderItem.color = color
        orderItem.quantity = qty
    elif action == 'add-remove':
        orderItem.quantity = value

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)


def deleteItem(request):
    data = json.loads(request.body)
    productId = data['productId']

    customer = request.user.customer
    product = get_object_or_404(Product, id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    orderItem.delete()

    return JsonResponse("Item was deleted", safe=False)
