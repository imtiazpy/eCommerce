from django.db import models
from wagtail.core.models import Page

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from home.blocks.headerCarousel import HeaderCarouselBlock


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
