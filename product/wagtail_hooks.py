from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from product.models import Order, Customer


class CustomerPageModelAdmin(ModelAdmin):
    model = Customer
    menu_label = 'Customer'
    menu_icon = 'folder-open-inverse'
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )


class OrderPageModelAdmin(ModelAdmin):
    model = Order
    menu_label = 'Order'
    menu_icon = 'folder-open-inverse'
    list_display = ('id', )
    list_filter = ('id', )
    search_fields = ('id', )


class CustomerAndOrderGroup(ModelAdminGroup):
    menu_label = 'Customers & Orders'
    menu_icon = 'folder-open-inverse'
    items = (CustomerPageModelAdmin, OrderPageModelAdmin)


modeladmin_register(CustomerAndOrderGroup)
