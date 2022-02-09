from django.db import models
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):

    def get_context(self, request):
        context = super().get_context(request)
        context['products'] = Product.objects.child_of(self).live()

        return context


class Product(Page):
    '''
    Model for Product
    '''
    sku = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('sku'),
        FieldPanel('price'),
        ImageChooserPanel('image'),
        FieldPanel('short_description'),
        InlinePanel('custom_fields',
                    label='Custom Fields'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        fields = []
        for f in self.custom_fields.get_object_list():
            if f.options:
                f.options_array = f.options.split(',')
                fields.append(f)
            else:
                fields.append(f)
        context['custom_fields'] = fields
        return context


class ProductCustomField(Orderable):
    product = ParentalKey('Product', on_delete=models.CASCADE,
                          related_name='custom_fields')
    name = models.CharField(max_length=255)
    options = models.CharField(max_length=500, null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('options'),
    ]
