from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

from contact.models import Contact


class ContactPageModelAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Contact'
    menu_icon = 'folder-open-inverse'
    list_display = ('first_name',)
    list_filter = ('first_name',)
    search_fields = ('first_name', )


modeladmin_register(ContactPageModelAdmin)
