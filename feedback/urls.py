from django.urls import path, include
from .views import get_feedback, give_feedback

urlpatterns = [
    path('<str:pk>/', get_feedback, name='feedbacks'),
    path('<str:pk>/create/', give_feedback, name='give_feedback')
]
