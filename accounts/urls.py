from django.urls import path
from .views import StudentSignUpView

urlpatterns = [
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
]
