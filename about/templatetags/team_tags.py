from atexit import register
from django import template

from about.models import TeamInfo

register = template.Library()


@register.simple_tag()
def get_team_info():
    return TeamInfo.objects.all()
