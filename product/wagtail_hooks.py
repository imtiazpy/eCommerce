from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from product.models import Order, Customer, OrderItem


class CustomerPageModelAdmin(ModelAdmin):
    model = Customer
    menu_label = 'Customer'
    menu_icon = 'folder-open-inverse'
    list_display = ('name', 'get_order')
    list_filter = ('name', )
    search_fields = ('name', )


class OrderPageModelAdmin(ModelAdmin):
    model = Order
    menu_label = 'Order'
    menu_icon = 'folder-open-inverse'
    list_display = ('id', 'items_in_order', 'get_cart_items')
    list_filter = ('id', )
    search_fields = ('id', )


class OrderItemPageModelAdmin(ModelAdmin):
    model = OrderItem
    menu_label = 'Order Item'
    menu_icon = 'folder-open-inverse'
    list_display = ('product', 'order', 'quantity')
    list_filter = ('product', )
    search_fields = ('product', )


class CustomerAndOrderGroup(ModelAdminGroup):
    menu_label = 'Customers & Orders'
    menu_icon = 'folder-open-inverse'
    items = (CustomerPageModelAdmin, OrderPageModelAdmin,
             OrderItemPageModelAdmin)


modeladmin_register(CustomerAndOrderGroup)
