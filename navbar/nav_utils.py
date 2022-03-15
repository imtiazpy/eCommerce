from django.db import models
from wagtail.core.models import Orderable

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel


# ================================
# Orderable
# ===============================
class OrderableMenuItem(Orderable):
    link_title = models.CharField(blank=True, null=True, max_length=50)
    link_url = models.CharField(blank=True, max_length=500)
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab")
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return "#"

    @property
    def text(self):
        if self.link_title:
            return self.link_title
        else:
            return " "

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page
        elif self.link_title:
            return self.link_title
        return "Missing Title"
