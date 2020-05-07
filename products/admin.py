from django.contrib import admin
from .models import Category, Brand, Item

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'slug', 'category',
                    'brand', 'best_seller', 'popular_item']
    list_filter = ['created', 'updated', 'best_seller', 'popular_item']
    list_editable = ['price', 'slug', 'best_seller', 'popular_item']
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_header = 'furniture store'
