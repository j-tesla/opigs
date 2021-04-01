from django.urls import path
from .views import *

urlpatterns = [
    path('', get_announcements, name='announcements'),
    path('create/', post_announcement, name='post_announcement'),
    path('update/<str:pk>', update_announcement, name='update_announcement'),
    path('delete/<str:pk>', delete_announcement, name='delete_announcement')
]
