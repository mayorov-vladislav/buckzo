from django.urls import path
from .views import ServicesPage

urlpatterns = [
    path('', ServicesPage.as_view(), name='services')
]
