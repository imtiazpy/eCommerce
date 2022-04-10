from django.shortcuts import render
from django.contrib import messages

from contact.models import Contact

from product.models import Order, Customer


def contact(request):
    custom_messages = []
    if request.method == 'POST':
        Contact.objects.create(
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            email=request.POST.get('email', ''),
            subject=request.POST.get('subject', ''),
            message=request.POST.get('message', ''),
        )
        custom_messages.append('Your message has been submitted')

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        cartItems = order.get_cart_items
        cartTotal = order.get_cart_total
    else:
        cartItems = 0
        cartTotal = 0
    context = {
        'contact': True,
        'cartItems': cartItems,
        'cartTotal': cartTotal,
        'custom_messages': custom_messages
    }
    return render(request, 'contact/contact.html', context=context)
