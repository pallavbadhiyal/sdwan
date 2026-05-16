from django.urls import path
from . import views

urlpatterns = [
    path('', views.devices_view, name='devices'),
    path('<str:system_ip>/', views.device_detail, name='device_detail'),
]