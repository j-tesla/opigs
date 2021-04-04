from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.http import HttpResponse

from .forms import StudentSignUpForm, CompanySignUpForm, AlumniSignUpForm
from .models import User
from notifications.models import Notification
from .decorators import student_required


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


def profile_redirect(request, pk=None):
    if pk is None:
        pk = request.user.id
        edit = True
    else:
        edit = False
    user = User.objects.get(id=pk)
    context = {"user": user, "edit": edit}
    if user.user_type == "STUDENT":
        return render(request, "accounts/student_profile.html", context=context)
    elif user.user_type == "COMPANY":
        return render(request, "accounts/company_profile.html", context=context)
    elif user.user_type == "ALUMNI":
        return render(request, "accounts/alumni_profile.html", context=context)

    return HttpResponse(200)


@login_required
def profile_update(request):
    User.objects.filter(id=request.user.id).update(**request.POST)
