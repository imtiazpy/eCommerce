from django.db import models
from wagtail.core.models import Page
from modelcluster.fields import ParentalKey

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import RichTextField, StreamField

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, StreamFieldPanel, InlinePanel

from about.about_utils import OrderableTeamInfo


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
