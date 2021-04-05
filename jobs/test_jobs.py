import pytest
from .models import JobPosting
from accounts.models import User,Company
from django.utils import timezone

@pytest.mark.django_db
def test_job_posting():
    user = User(name='Apple',user_type='company')
    user.save()
    company = Company.objects.create(user=user,email="apple@gmail.com",work_environment="Happy environment",recruitment_policy="Good practical skills")
    job = JobPosting.objects.create(job_type='placement',company=company,title='Software Engineer',date_posted=timezone.now(),deadline_date=timezone.now(),skills="Honest",industry='Software',branches='CSE,ECE,EE')
    assert job.job_type=='placement'
    assert job.title=='Software Engineer'
    assert job.skills=="Honest"
    assert job.industry=='Software'
    assert job.branches=='CSE,ECE,EE'