from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from contact.models import Contact

from product.models import Order, Customer


@login_required(login_url='/accounts/login')
def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            email=request.POST.get('email', ''),
            subject=request.POST.get('subject', ''),
            message=request.POST.get('message', ''),
        )
        messages.success(request, "Your message has been submitted.")
    try:
        customer = request.user.customer
    except:
        customer, created = Customer.objects.get_or_create(
            user=request.user, name=request.user.username, email=request.user.email)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    cartItems = order.get_cart_items
    cartTotal = order.get_cart_total
    context = {
        'contact': True,
        'cartItems': cartItems,
        'cartTotal': cartTotal
    }
    return render(request, 'contact/contact.html', context=context)
