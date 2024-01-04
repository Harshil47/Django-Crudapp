# sanghavi/urls.py
from django.urls import path
from .views import add_data, success

urlpatterns = [
    path('add/', add_data, name='add_data'),
    path('success/', success, name='success'),
]
