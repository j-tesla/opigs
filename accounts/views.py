from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.http import HttpResponse

from .forms import StudentSignUpForm, CompanySignUpForm, AlumniSignUpForm
from .models import User
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
        return redirect('students:dashboard')


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
        notification.users.add(admin)
        return redirect('companies:dashboard')


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
        return redirect('profile')


@login_required
def profile_redirect(request, pk):
    user = User.objects.get(id=pk)
    edit = False
    if request.user.id == pk:
        edit = True
    context = {"user": user, "edit": edit}
    if user.user_type == "STUDENT":
        return render(request, "profiles/student.html", context=user)
    elif user.user_type == "COMPANY":
        return render(request, "profiles/company.html", context=user)
    elif user.user_type == "ALUMNI":
        return render(request, "profiles/alumni.html", context=user)

    return HttpResponse(200)

@login_required
def profile_update(request):
    User.objects.filter(id = request.user.id).update(**request.POST)
