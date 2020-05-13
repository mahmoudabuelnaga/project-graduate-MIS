from django.urls import path, include
from .views import OrderView, add_to_cart, remove_from_cart, remove_single_item_from_cart, order_confirmation
app_name = 'orders'

urlpatterns = [
    path('order-summary/', OrderView.as_view(), name='order_summary'),

    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),

    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),

    path('remove-item-from-cart/<slug>/',
         remove_single_item_from_cart, name='remove_single_item_from_cart'),
]
