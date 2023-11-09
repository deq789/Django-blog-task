from django.urls import path
from .views import ContactView

app_name = 'apps.contact'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact_view'),
]
