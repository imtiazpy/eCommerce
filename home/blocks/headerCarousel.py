from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeaderCarouselBlock(blocks.StructBlock):
    heading = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=True)
