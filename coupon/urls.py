from django.urls import path, include
from .views import AddCouponView
app_name = 'coupon'

urlpatterns = [
    path('coupon/', AddCouponView.as_view(), name="add_coupon"),
]
