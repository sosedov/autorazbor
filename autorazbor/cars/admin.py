from django.contrib import admin

from .models import CarMark, CarModel, CarSubmodel


class ModelsInLine(admin.StackedInline):
    model = CarModel
    extra = 1


@admin.register(CarMark)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'changed')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = ('created', 'changed',)
    inlines = [ModelsInLine]


class ModelsInLine(admin.StackedInline):
    model = CarSubmodel
    extra = 1


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'changed')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = ('created', 'changed',)
    readonly_fields = ('created', 'changed',)
    inlines = [ModelsInLine]


@admin.register(CarSubmodel)
class CarSubmodelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'changed')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = ('created', 'changed',)
