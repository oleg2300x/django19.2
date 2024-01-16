from django.contrib import admin

from catalog.models import Category, Product, Version


# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category',)
    search_fields = ('name_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_published',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_number', 'version_name', 'is_active',)
    list_filter = ('is_active',)
    # search_fields = ('name', 'description',)
