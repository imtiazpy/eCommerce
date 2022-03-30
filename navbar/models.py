from django.db import models
from modelcluster.models import ClusterableModel

from wagtail.snippets.models import register_snippet

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.fields import ParentalKey

from navbar.nav_utils import OrderableMenuItem


# =================================================
# Navigation and its item (Ancestor and Decedents)
# ===================================================
@register_snippet
class NavTopLevelItem(ClusterableModel):
    """
    Snippet for site navigation bars
    """
    class Meta:
        verbose_name = ("Top Level Item")
    name = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name=("Navigation Name")
    )
    main_link = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name=("Main Navigation Link")
    )
    position = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(
        default=False,
        verbose_name=("Is Active")
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("main_link"),
        FieldPanel("is_active"),
        FieldPanel("position")
    ]

    def __str__(self):
        return self.name


# ===================================
# Mega menu and its item
# ===================================

class MegaMenuItem(OrderableMenuItem):
    page = ParentalKey("MegaMenu", related_name="mega_menu_items")


@register_snippet
class MegaMenu(ClusterableModel):
    navigation = ParentalKey("NavTopLevelItem", related_name="mega_menu")

    title = models.CharField(
        blank=True,
        null=True,
        max_length=100
    )
    mega_menu_link = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name=("Mega Menu Link")
    )
    panels = [
        SnippetChooserPanel("navigation"),
        MultiFieldPanel([
            FieldPanel('title')
        ], heading="Mega Menu"),
        FieldPanel('mega_menu_link'),
        InlinePanel("mega_menu_items", label="Mega Menu Item")
    ]

    def __str__(self):
        return self.title
