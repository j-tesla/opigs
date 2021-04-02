from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import company_required
from .models import *
from .forms import JobPostingForm
from accounts.models import Company

# Create your views here.

@login_required
def get_jobs(request):
    jobs = JobPosting.objects.all()

    context = {"joblist": jobs}

    return render(request, 'jobs/jobs.html', context=context)


@login_required
@company_required
def post_job(request):
    form = JobPostingForm()
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        # todo company linking
        form.company = Company.objects.get(id=request.user)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    context = {'form': form}
    return render(request, 'form.html', context=context)

