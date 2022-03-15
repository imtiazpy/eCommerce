from atexit import register
from django import template

from navbar.models import NavTopLevelItem

register = template.Library()


@register.simple_tag()
def get_navbar():
    return NavTopLevelItem.objects.filter(is_active=True).order_by("position")
