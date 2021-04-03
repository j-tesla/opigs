from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', get_jobs, name='jobs'),
    path('post/', post_job, name='post_job'),
    path('update/<str:pk>/', update_job, name='update_job'),
    path('delete/<str:pk>/', delete_job, name='delete_job')
]