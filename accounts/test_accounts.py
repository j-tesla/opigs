import pytest
from .models import Student,User,Company,Alumni,Admin

@pytest.mark.django_db
def test_user():
    user = User(name='Apple',user_type='company')
    assert user.name=='Apple'
    assert user.user_type=='company'

@pytest.mark.django_db
def test_student():
    user = User(name='Apple',user_type='student')
    user.save()
    student = Student.objects.create(user=user,email="apple@gmail.com",phone="9898989898",date_of_birth="2001-11-08",department="Computer Science and Engineering")
    assert student.email=="apple@gmail.com"
    assert student.phone=="9898989898"
    assert student.date_of_birth=="2001-11-08"
    assert student.department=="Computer Science and Engineering"

@pytest.mark.django_db
def test_company():
    user = User(name='Apple',user_type='company')
    user.save()
    company = Company.objects.create(user=user,email="apple@gmail.com",work_environment="Happy environment",recruitment_policy="Good practical skills")
    assert company.email=="apple@gmail.com"
    assert company.work_environment=="Happy environment"
    assert company.recruitment_policy=="Good practical skills"

@pytest.mark.django_db
def test_alumni():
    user = User(name='Apple',user_type='alumni')
    user.save()
    alumni = Alumni.objects.create(user=user,email="apple@gmail.com")
    assert alumni.email=="apple@gmail.com"


