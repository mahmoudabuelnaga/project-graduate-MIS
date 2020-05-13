from django.urls import path, include
from .views import RequestRefundView
app_name = 'refound'


urlpatterns = [
    path('request-refound/', RequestRefundView.as_view(), name='request-refound')
]
