from django.urls import path
from .views import HomeView, SuccessView

app_name = 'apps.home'

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('success/', SuccessView.as_view(), name='success_view'),
]
