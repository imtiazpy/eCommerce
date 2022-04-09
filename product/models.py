from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from product.blocks.productImage import ProductImageBlock


class AllProductListingPage(Page):
    """Model to list all the products in one page"""
    template = 'product/all_product_listing_page.html'
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
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            cartItems = order.get_cart_items
            cartTotal = order.get_cart_total
        else:
            order = {'id': 0}
            cartItems = 0
            cartTotal = 0

        context = super().get_context(request)
        context['products'] = Product.objects.all().live()
        context['cartItems'] = cartItems
        context['cartTotal'] = cartTotal
        return context


class ProductIndex(Page):
    """Model to list all child products created under this Page"""
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
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            cartItems = order.get_cart_items
            cartTotal = order.get_cart_total
        else:
            order = {'id': 0}
            cartItems = 0
            cartTotal = 0

        context = super().get_context(request)
        context['products'] = Product.objects.child_of(self).live()
        context['cartItems'] = cartItems
        context['cartTotal'] = cartTotal
        return context


class Product(Page):
    """Model for product detail page"""
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
        if request.user.is_authenticated:
            customer = request.user.customer
            productId = self.id
            order, created = Order.objects.get_or_create(
                customer=customer, complete=False)
            orderItem, created = OrderItem.objects.get_or_create(
                product_id=productId, order=order)

            cartItems = order.get_cart_items
            cartTotal = order.get_cart_total
            orderQuantity = orderItem.quantity
        else:
            order = {'id': 0}
            cartItems = 0
            cartTotal = 0
            orderQuantity = 0

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
        context['cartItems'] = cartItems
        context['cartTotal'] = cartTotal
        context['orderQuantity'] = orderQuantity
        return context

    def __str__(self):
        return self.custom_title


# =================models for customer, Order, OrderItem and Shipping==============

class Customer(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)

    def __str__(self):
        return self.name

    @property
    def get_order(self):
        """To show all the orders of the customer in wagtail modelAdmin"""
        orders = [item for item in self.order_set.all()]
        return orders


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        """To show the sum of each orderitems total(quantity*price)"""
        ordered_items = self.orderitem_set.all()
        total = sum([item.get_total for item in ordered_items])
        return total

    @property
    def get_cart_items(self):
        """To show the sum of all the items quantity in cart and checkout"""
        ordered_items = self.orderitem_set.all()
        total = sum([item.quantity for item in ordered_items])
        return total

    @property
    def items_in_order(self):
        """To show all the orderitems of order and each ones quantity in wagtail modelAdmin"""
        ordered_items = self.orderitem_set.all()
        items = [(item.product.custom_title, item.quantity)
                 for item in ordered_items]
        return items


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.custom_title

    @property
    def get_total(self):
        """To show the total of each order item (quantity * price)"""
        total = self.product.new_price * self.quantity
        return total


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
