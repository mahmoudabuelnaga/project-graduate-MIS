from django.urls import path, include
from .views import SearchItemView
app_name = 'search'

urlpatterns = [
    path('search/products/', SearchItemView.as_view(), name='search_products'),
]
