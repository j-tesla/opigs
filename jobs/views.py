from django.shortcuts import render
from .models import *


# Create your views here.

def get_jobs(request):
    jobs = JobPosting.objects.all()

    context = {"joblist": jobs}

    return render(request, 'jobs/jobs.html', context=context)

# def post_job(request):
#     job = JobPosting.objects.get()
#     # todo
