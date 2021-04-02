from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Student

class StudentSignUpForm(UserCreationForm):

  dob = forms.DateField(required=True)
  phone = forms.CharField(max_length=15)

  class Meta(UserCreationForm.Meta):
    model = User

  @transaction.atomic
  def save(self):
    user = super().save(commit=False)
    user.is_student = True
    user.save()
    student = Student.objects.create(user=user, dob=dob, phone=phone)
    return user