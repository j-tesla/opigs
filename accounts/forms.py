from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Student, Company, Admin, Alumni


class StudentSignUpForm(UserCreationForm):
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
                               resume=self.cleaned_data.get('resume')
                               )
        return user


class CompanySignUpForm(UserCreationForm):
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
                               other_details=self.cleaned_data.get('other_details'))
        return user


class AlumniSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=200)
    companies_worked_in = forms.ModelMultipleChoiceField(
        queryset=Company.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
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
        alumni.companies_worked_in.add(*self.cleaned_data.get('companies'))
        return user
