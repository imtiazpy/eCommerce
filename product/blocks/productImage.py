from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ProductImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
