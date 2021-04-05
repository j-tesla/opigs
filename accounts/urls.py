from django.urls import path, include
from .views import StudentSignUpView, CompanySignUpView, AlumniSignUpView, profile, signup, home
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=UserLoginForm),
         name='login'),
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls'), name='django_auth'),
    path('profile/', profile, name='my_profile'),
    path('profile/<str:pk>', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('signup/students/', StudentSignUpView.as_view(), name='students_signup'),
    path('signup/companies/', CompanySignUpView.as_view(), name='companies_signup'),
    path('signup/alumni/', AlumniSignUpView.as_view(), name='alumni_signup'),

]
