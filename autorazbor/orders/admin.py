from django.contrib import admin

from .models import Order, Order_Items


admin.site.register(Order)

admin.site.register(Order_Items)