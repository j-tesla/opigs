from django.db import models
from accounts.models import Company


# Create your models here.


class JobPosting(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    JOBTYPE = [('INTERNSHIP', 'internship'), ('PLACEMENT', 'placement')]
    title = models.CharField(max_length=100, null=False)
    job_type = models.CharField(max_length=30, choices=JOBTYPE, null=False)
    date_posted = models.DateTimeField(auto_now=True)
    skills = models.TextField(null=False)
    description = models.TextField(null=True)
    industry = models.CharField(max_length=100, null=False)
    branch_restriction = models.BooleanField(default=False)
    branches = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
