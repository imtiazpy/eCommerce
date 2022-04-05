from django.shortcuts import render


def cart(request):
    context = {

    }

    return render(request, 'product/cart.html', context)


def checkout(request):
    context = {

    }

    return render(request, 'product/checkout.html', context)
