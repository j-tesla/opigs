from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.http import HttpResponseNotFound

from .forms import StudentSignUpForm, CompanySignUpForm, AlumniSignUpForm
from .models import *
from notifications.models import Notification


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'STUDENT'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('my_profile')


class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'COMPANY'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        admin = User.objects.filter(user_type="ADMIN")[0]
        notification = Notification(content='New Company: ' + user.name, url=f'/profile/{user.id}')
        notification.save()
        notification.users.add(admin)
        return redirect('my_profile')


class AlumniSignUpView(CreateView):
    model = User
    form_class = AlumniSignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ALUMNI'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('my_profile')


@login_required
def profile(request, pk=None):
    if pk is None:
        pk = request.user.id
        edit = True
        if request.method == 'POST':
            if pk != request.user.id and request.user.user_type == 'ADMIN':
                print('verified')
                user = User.objects.get(id=pk)
                user.company.verified = True
                user.company.save()
                return redirect(request, 'profile', pk)
            user = User.objects.get(id=pk)
            user.name = request.POST['name']
            user.save()
            if user.user_type == 'STUDENT':
                student = Student.objects.get(user=user.id)
                student.email = request.POST['email']
                student.department = request.POST['department']
                student.phone = request.POST['phone']
                student.date_of_birth = request.POST['date_of_birth']

                if 'resume' in request.FILES.keys():
                    student.resume = request.FILES['resume']

                student.save()
            
            if user.user_type == 'COMPANY':
                company = Company.objects.get(user=user.id)
                company.email = request.POST['email']
                company.work_environment = request.POST['work_environment']
                company.recruitment_policy = request.POST['recruitment_policy']
                company.other_details = request.POST['other_details']

                company.save()

            if user.user_type == "ALUMNI":
                alumni = Alumni.objects.get(user=user.id)
                alumni.email = request.POST["email"]
                alumni.companies_worked_in = request.POST["companies_worked_in"]

    else:
        edit = False
    user = User.objects.get(id=pk)
    context = {"user": user, "edit": edit, "viewer": request.user}
    if user.user_type == "STUDENT":
        return render(request, "accounts/student_profile.html", context=context)
    elif user.user_type == "COMPANY":
        return render(request, "accounts/company_profile.html", context=context)
    elif user.user_type == "ALUMNI":
        return render(request, "accounts/alumni_profile.html", context=context)
    else:
        return HttpResponseNotFound()


def signup(request):
    context = {}
    return render(request, 'accounts/signup_home.html', context=context)


def home(request):
    context = {}
    return render(request, 'home.html', context=context)
