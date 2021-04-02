from django.contrib import admin
from .models import User, Student, Company, Alumni, Admin

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Alumni)
admin.site.register(Company)
