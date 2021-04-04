from django.urls import path, include
from .views import StudentSignUpView, CompanySignUpView, AlumniSignUpView, profile_redirect, student_profile

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='django_auth'),
    path('profile/', profile_redirect, name='profile_redirect'),
    path('profile/student', student_profile, name='student_profile'),
    path('signup/students/', StudentSignUpView.as_view(), name='students_signup'),
    path('signup/companies/', CompanySignUpView.as_view(), name='companies_signup'),
    path('signup/alumni/', AlumniSignUpView.as_view(), name='alumni_signup'),

]
