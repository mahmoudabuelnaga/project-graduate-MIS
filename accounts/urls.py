from django.urls import path, include
from . import views
app_name = 'accounts'

urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
]
