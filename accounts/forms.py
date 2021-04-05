from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction

from .models import User, Student, Company, Admin, Alumni


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=200)
    date_of_birth = forms.DateField(required=True)
    phone = forms.CharField(max_length=15)
    department = forms.ChoiceField(choices=Student.DEPARTMENTS)
    resume = forms.FileField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.name = self.cleaned_data.get('name')
        user.user_type = 'STUDENT'
        user.save()
        Student.objects.create(user=user, date_of_birth=self.cleaned_data.get('date_of_birth'),
                               phone=self.cleaned_data.get('phone'),
                               department=self.cleaned_data.get('department'),
                               resume=self.cleaned_data.get('resume'),
                               email=self.cleaned_data.get('email')
                               )
        return user


class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=200)
    work_environment = forms.CharField(widget=forms.Textarea)
    recruitment_policy = forms.CharField(widget=forms.Textarea)
    other_details = forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.name = self.cleaned_data.get('name')
        user.user_type = 'COMPANY'
        user.save()
        Company.objects.create(user=user, work_environment=self.cleaned_data.get('work_environment'),
                               recruitment_policy=self.cleaned_data.get('recruitment_policy'),
                               other_details=self.cleaned_data.get('other_details'),
                               email=self.cleaned_data.get('email'))
        return user


class AlumniSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(required=True)
    companies_worked_in = forms.ModelMultipleChoiceField(
        queryset=Company.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.name = self.cleaned_data.get('name')
        user.user_type = 'ALUMNI'
        user.save()
        alumni = Alumni.objects.create(user=user)
        alumni.companies_worked_in.add(*self.cleaned_data.get('companies_worked_in'))
        return user


class UserLoginForm(AuthenticationForm):
    def init(self, args, **kwargs):
        super(UserLoginForm, self).init(args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user',
               'placeholder': 'Enter username...',
               'id': 'inputUsername', }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Enter password...',
            'id': 'inputPassword',
        }
    ))
