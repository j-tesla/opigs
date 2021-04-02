from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

alphabetic = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.
class User(AbstractUser):
  name = models.CharField(max_length=200, validators = [alphabetic])
  email = models.EmailField(unique=True)
  USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'company'),
      (3, 'alumni'),
      (4, 'admin')
  )
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ['name', 'user_type']

class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  dob = models.DateTimeField()
  phone = models.CharField(max_length=15)

  DEPARTMENTS = (
    (1, 'Computer Science and Engineering'),
    (2, 'Electrical Engineering'),
    (3, 'Electronics and Electrical Communication Engineering')
  )

  department = models.CharField(max_length=200, choices=DEPARTMENTS)

class Company(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  work_environment = models.TextField()
  recruitment_policy = models.TextField()
  verified = models.BooleanField(default=False)
  other_details = models.TextField()

class Alumni(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  companies = models.ManyToManyField(Company)

class Admin(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  def save(self, *args, **kwargs):
    if not self.pk and Admin.objects.exists():
        raise ValidationError('There is can be only one Admin instance')
    return super(Admin, self).save(*args, **kwargs)
