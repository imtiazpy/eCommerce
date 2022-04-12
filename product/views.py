from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
import datetime

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
        cartItems = 0
        cartTotal = 0

    # for Continue-Shopping button in cart page
    """
    it works when we don't increase or decrease any item, but since we reload the page everytime when we increace or decrease any orderItem in cart page, the preUrl sets to the cart page. so it will perfectly as soon as we save cart data in cookies, doing so we don't have to reload the page.
    """
    preUrl = request.META.get('HTTP_REFERER')

    context = {
        'items': items,
        'cartItems': cartItems,
        'cartTotal': cartTotal,
        'preUrl': preUrl
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
        cartItems = 0
        cartTotal = 0
    context = {
        'items': items,
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


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        total = data['userData']['total']

        if total != 0 and data['shippingFormData']['phone'] != '':
            order.transaction_id = transaction_id

            # total needs to be validated
            # if total == order.get_cart_total:
            #     order.complete = True
            order.complete = True

            order.save()

            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shippingFormData']['address'],
                city=data['shippingFormData']['city'],
                zipcode=data['shippingFormData']['zipcode'],
                phone=data['shippingFormData']['phone'],
                additional_info=data['shippingFormData']['additionalInfo'],
            )
        else:
            # Todo: we will show some message
            print("=======No items added===========")
    else:
        print("You're not logged in")

    return JsonResponse("Order is Complete", safe=False)
