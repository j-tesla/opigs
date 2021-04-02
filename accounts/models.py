from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

alphabetic = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')


class User(AbstractUser):
    name = models.CharField(max_length=200, validators=[alphabetic])
    USER_TYPE_CHOICES = (
        ('STUDENT', 'Student'),
        ('COMPANY', 'Company'),
        ('ALUMNI', 'Alumni'),
        ('ADMIN', 'Admin'),
        ('SUPERUSER', 'SuperUser')
    )
    user_type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES)
    # USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'user_type']


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)

    DEPARTMENTS = (
        (1, 'Computer Science and Engineering'),
        (2, 'Electrical Engineering'),
        (3, 'Electronics and Electrical Communication Engineering')
    )

    department = models.CharField(max_length=200, choices=DEPARTMENTS)

    def __str__(self):
        return self.user.name


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    work_environment = models.TextField(blank=True)
    recruitment_policy = models.TextField()
    verified = models.BooleanField(default=False)
    other_details = models.TextField(blank=True)

    def __str__(self):
        return self.user.name


class Alumni(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    companies_worked_in = models.ManyToManyField(Company)

    def __str__(self):
        return self.user.name


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.pk and Admin.objects.exists():
            raise ValidationError('There is can be only one Admin instance')
        return super(Admin, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.name
