from django import template
from wagtail.core.models import Page, Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return Site.find_for_request(context['request']).root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.inclusion_tag('home/tags/site_header.html', takes_context=True)
def get_site_header(context):
    return context


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('home/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    queryset = parent.get_children()
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(
            menuitem.url) if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request']
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('home/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()

    for menuitem in menuitems_children:
        # Check if menuitem has children
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (calling_page.url.startswith(
            menuitem.url) if calling_page else False)

    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request']
    }


@register.inclusion_tag('home/tags/submenu.html', takes_context=True)
def submenu(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()

    for menuitem in menuitems_children:
        # Check if menuitem has children
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)

    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
