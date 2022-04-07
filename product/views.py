from django.shortcuts import render

from product.models import Customer, Order, OrderItem, ShippingAddress


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'id': 0}
    context = {
        'items': items,
        'order': order,
    }

    return render(request, 'product/cart.html', context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'id': 0}
    context = {
        'items': items,
        'order': order
    }

    return render(request, 'product/checkout.html', context)
