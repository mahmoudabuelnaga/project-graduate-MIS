from django.urls import path, include
from .views import CheckoutView

app_name = 'address'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
