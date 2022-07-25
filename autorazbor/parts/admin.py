from django.contrib import admin

from .models import PartCategory, Parts, PartSubCategory


class SubCategoryInLine(admin.StackedInline):
    model = PartSubCategory
    extra = 1


@admin.register(PartCategory)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'changed')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = ('created', 'changed',)
    inlines = [SubCategoryInLine]


@admin.register(PartSubCategory)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'changed')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = ('created', 'changed',)


@admin.register(Parts)
class CarMarkAdmin(admin.ModelAdmin):
    list_display = ('part_subcategory', 'car_submodel', 'price', 'created', 'changed', )
    list_display_links = ('part_subcategory',)
    list_filter = ('part_subcategory',)
    search_fields = ('part_subcategory',)
    readonly_fields = ('created', 'changed',)
    


#admin.site.register(PartSubCategory)

#admin.site.register(PartCategory)

#admin.site.register(Parts)