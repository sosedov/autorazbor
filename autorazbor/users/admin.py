from django.contrib import admin

from .models import User, Tariff


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone',)
    list_display_links = ('username', 'phone',)
    list_filter = ('username', 'phone',)
    search_fields = ('username', 'phone',)


@admin.register(Tariff)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created', 'changed')
    list_display_links = ('name', 'value',)
    list_filter = ('name',)
    search_fields = ('name', 'phone', 'created', 'changed',)