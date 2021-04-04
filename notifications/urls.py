from django.urls import path
from .views import get_notifications, delete_notification, clear_notifications

urlpatterns = [
    path('', get_notifications, name='notifications'),
    path('delete/<str:pk>/', delete_notification, name='delete_notification'),
    path('clear/', clear_notifications, name='clear_notifications')
]
