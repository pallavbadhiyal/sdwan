from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.devices_view, name='devices'),
]