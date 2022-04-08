from django.db import models
from wagtail.core.models import Page

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from home.blocks.headerCarousel import HeaderCarouselBlock

from product.models import Product, Order, Customer


class HomePage(Page):

    header_carousel = StreamField([
        ('carousel', HeaderCarouselBlock()),
    ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('header_carousel')
    ]

    def get_context(self, request):
        if request.user.is_authenticated:
            try:
                customer = request.user.customer
            except:
                customer, created = Customer.objects.get_or_create(
                    user=request.user, name=request.user.username, email=request.user.email)
            # customer = request.user.customer
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            cartItems = order.get_cart_items
            cartTotal = order.get_cart_total
        else:
            order = {'id': 0}
            cartItems = 0
            cartTotal = 0

        context = super().get_context(request)
        context['featured'] = Product.objects.filter(is_featured=True)
        context['cartItems'] = cartItems
        context['cartTotal'] = cartTotal

        return context
