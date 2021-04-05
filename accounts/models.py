from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

alphabetic = RegexValidator(r'^[a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')

def vaildate_fields(value):
    print(value)
    if not value:
        raise ValidationError("This field cannot be empty!")
    else:
        return value


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
    email = models.EmailField(validators=[vaildate_fields],blank=False)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='documents/')

    DEPARTMENTS = (
        (1, 'Aerospace Engineering'),
        (2, 'Agricultural and Food Engineering'),
        (3, 'Architecture and Regional Planning'),
        (4, 'Bio Science'),
        (5, 'Biotechnology'),
        (6, 'Chemical Engineering'),
        (7, 'Chemistry'),
        (8, 'Civil Engineering'),
        (9, 'Computer Science and Engineering'),
        (10, 'Electrical Engineering'),
        (11, 'Electronics and Electrical Communication Engg.'),
        (12, 'Geology and Geophysics'),
        (13, 'Humanities and Social Sciences'),
        (14, 'Industrial and Systems Engineering'),
        (15, 'Mathematics'),
        (16, 'Mechanical Engineering'),
        (17, 'Metallurgical and Materials Engineering'),
        (18, 'Mining Engineering'),
        (19, 'Ocean Engg and Naval Architecture'),
        (20, 'Physics'),
    )

    department = models.CharField(max_length=200, choices=DEPARTMENTS)

    def __str__(self):
        return self.user.name


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(null=False)
    work_environment = models.TextField(blank=True)
    recruitment_policy = models.TextField()
    verified = models.BooleanField(default=False)
    other_details = models.TextField(blank=True)

    def __str__(self):
        return self.user.name


class Alumni(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    companies_worked_in = models.ManyToManyField(Company)
    email = models.EmailField(null=False)

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
