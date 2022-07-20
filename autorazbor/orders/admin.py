from django.contrib import admin

from .models import Order, Order_Items


class OrderItemsInLine(admin.StackedInline):
    model = Order_Items
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('manager', 'customer', 'created', 'changed')
    list_display_links = ('manager', 'customer',)
    list_filter = ('manager',)
    search_fields = ('manager',)
    readonly_fields = ('created', 'changed',)
    inlines = [OrderItemsInLine]


@admin.register(Order_Items)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'part', 'created', 'changed')
    list_display_links = ('order', 'part',)
    list_filter = ('order', 'part',)
    search_fields = ('order', 'part',)
    readonly_fields = ('created', 'changed',)