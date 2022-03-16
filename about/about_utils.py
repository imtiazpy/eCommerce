from django.db import models
from wagtail.core.models import Orderable

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class OrderableTeamInfo(Orderable):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    title = models.CharField(null=True, blank=True, max_length=255)
    details = models.CharField(null=True, blank=True, max_length=500)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('details')
    ]
