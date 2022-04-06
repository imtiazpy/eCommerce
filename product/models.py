from django.db import models
from django.contrib.auth import get_user_model

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from product.blocks.productImage import ProductImageBlock


class ProductIndex(Page):
    """Model to list all the products"""
    template = 'product/product_index.html'
    custom_title = models.CharField(max_length=100, blank=False, null=True)
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        ImageChooserPanel('banner')
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['products'] = Product.objects.child_of(self).live()
        return context


class Product(Page):
    """Model for product"""
    template = 'product/product.html'
    custom_title = models.CharField(max_length=100, blank=False, null=True)
    sku = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    old_price = models.DecimalField(
        decimal_places=2, max_digits=10, null=True, blank=True)

    new_price = models.DecimalField(decimal_places=2, max_digits=10)

    """Single image to show in the homepage and product listing page"""
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    """Multiple images to show in product detail page"""
    product_images = StreamField([
        ('images', ProductImageBlock()),
    ], null=True, blank=True)

    is_available = models.BooleanField(
        default=False, verbose_name=("Is Available")
    )
    is_featured = models.BooleanField(
        default=False, verbose_name=("Is Featured")
    )

    available_sizes = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        help_text="Add available sizes with coma. ie: S,M,L"
    )
    available_colors = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        help_text="Add available colors with coma. ie:Red,Green,Blue"
    )

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        FieldPanel('sku'),
        FieldPanel('old_price'),
        FieldPanel('new_price'),
        ImageChooserPanel('featured_image'),
        StreamFieldPanel('product_images'),
        FieldPanel('description', classname="full"),
        FieldPanel('is_available'),
        FieldPanel('is_featured'),
        FieldPanel('available_sizes'),
        FieldPanel('available_colors'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        sizes = []
        colors = []
        if self.available_sizes:
            for size in self.available_sizes.split(','):
                sizes.append(size)
        if self.available_colors:
            for color in self.available_colors.split(','):
                colors.append(color)
        context['sizes'] = sizes
        context['colors'] = colors
        return context


# =================models for customer, Order, OrderItem and Shipping==============

class Customer(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.custom_title


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
