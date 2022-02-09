from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SnipcartSettings(BaseSetting):
    api_key = models.CharField(
        max_length=255,
        help_text='Your Snipcart public API key'
    )
