# Generated by Django 3.1.7 on 2021-04-05 03:59

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')])),
                ('user_type', models.CharField(choices=[('STUDENT', 'Student'), ('COMPANY', 'Company'), ('ALUMNI', 'Alumni'), ('ADMIN', 'Admin'), ('SUPERUSER', 'SuperUser')], max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('email', models.EmailField(max_length=254)),
                ('work_environment', models.TextField(blank=True)),
                ('recruitment_policy', models.TextField()),
                ('verified', models.BooleanField(default=False)),
                ('other_details', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('resume', models.FileField(upload_to='documents/')),
                ('department', models.CharField(choices=[(1, 'Aerospace Engineering'), (2, 'Agricultural and Food Engineering'), (3, 'Architecture and Regional Planning'), (4, 'Bio Science'), (5, 'Biotechnology'), (6, 'Chemical Engineering'), (7, 'Chemistry'), (8, 'Civil Engineering'), (9, 'Computer Science and Engineering'), (10, 'Electrical Engineering'), (11, 'Electronics and Electrical Communication Engg.'), (12, 'Geology and Geophysics'), (13, 'Humanities and Social Sciences'), (14, 'Industrial and Systems Engineering'), (15, 'Mathematics'), (16, 'Mechanical Engineering'), (17, 'Metallurgical and Materials Engineering'), (18, 'Mining Engineering'), (19, 'Ocean Engg and Naval Architecture'), (20, 'Physics')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('email', models.EmailField(max_length=254)),
                ('companies_worked_in', models.ManyToManyField(to='accounts.Company')),
            ],
        ),
    ]
