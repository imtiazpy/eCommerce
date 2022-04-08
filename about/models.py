from django.db import models
from wagtail.core.models import Page
from modelcluster.fields import ParentalKey

from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel

from about.about_utils import OrderableTeamInfo

from product.models import Order, Customer


class TeamInfo(OrderableTeamInfo):
    info = ParentalKey('About', related_name='team_info')


class About(Page):
    '''
    Model for About page
    '''
    heading = models.CharField(blank=True, null=True, max_length=255)
    description = RichTextField()

    secondary_heading = models.CharField(blank=True, null=True, max_length=255)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('heading'),
            FieldPanel('description')
        ],
            heading="About Company"
        ),
        MultiFieldPanel([
            FieldPanel('secondary_heading'),
            InlinePanel('team_info', label="Team Info")
        ], heading="About Team")
    ]

    def __str__(self):
        return self.heading

    def get_context(self, request):
        if request.user.is_authenticated:
            try:
                customer = request.user.customer
            except:
                customer, created = Customer.objects.get_or_create(
                    user=request.user, name=request.user.username, email=request.user.email)
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            cartItems = order.get_cart_items
            cartTotal = order.get_cart_total
        else:
            order = {'id': 0}
            cartItems = 0
            cartTotal = 0

        context = super().get_context(request)
        context['cartItems'] = cartItems
        context['cartTotal'] = cartTotal
        return context
