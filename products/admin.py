from django.contrib import admin
from .models import Category, Brand, Item

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_prem('categories.read_category'):
            return [f.title for f in self.model._meta.fields]

        return super(CategoryAdmin, self).get_readonly_fields(request, obj=obj) 


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
