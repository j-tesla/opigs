from django.urls import path
from .views import get_notifications, delete_notification

urlpatterns = [
    path('', get_notifications, name='notifications'),
    path('<str:pk>', delete_notification, name='delete_notification')
]
