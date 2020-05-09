from django.urls import path, include
from .views import product_list_by_category, product_list_by_brand, ItemDetailView, home
app_name = 'products'

urlpatterns = [
    path('', home, name='home'),

    path('category/products/', product_list_by_category,
         name='product_list_category'),

    path('category/products/<slug:category_slug>/',
         product_list_by_category, name='product_list_by_category'),

    path('brand/products/', product_list_by_brand, name='product_list_brand'),

    path('brand/products/<slug:brand_slug>/',
         product_list_by_brand, name='product_list_by_brand'),

    path('products/<id>/<slug>/', ItemDetailView.as_view(), name='product_detail'),

]
