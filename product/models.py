from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel


class ProductIndex(Page):
    '''
    Model to list all the products
    '''
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
    '''
    Model for Product
    '''
    template = 'product/product.html'
    custom_title = models.CharField(max_length=100, blank=False, null=True)
    sku = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    old_price = models.DecimalField(
        decimal_places=2, max_digits=10, null=True, blank=True)
    new_price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    is_available = models.BooleanField(
        default=False, verbose_name=("Is Available")
    )
    is_featured = models.BooleanField(
        default=False, verbose_name=("Is Featured")
    )

    available_sizes = models.CharField(max_length=500, null=True, blank=True)
    available_colors = models.CharField(max_length=500, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        FieldPanel('sku'),
        FieldPanel('old_price'),
        FieldPanel('new_price'),
        ImageChooserPanel('image'),
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
        for size in self.available_sizes.split(','):
            sizes.append(size)
        for color in self.available_colors.split(','):
            colors.append(color)
        context['sizes'] = sizes
        context['colors'] = colors
        return context
