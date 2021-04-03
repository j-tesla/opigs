from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import company_required
from .models import JobPosting
from .forms import JobPostingForm
from accounts.models import Company
from django.http import HttpResponse

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
        form.company = Company.objects.get(id=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('jobs')
    context = {'form': form}
    return render(request, 'form.html', context=context)

@login_required
@company_required
def update_job(request, pk):
    job = JobPosting.objects.get(id=pk)
    if request.user.id != job.company.user.id:
        return HttpResponse("Unauthorized Access", 403)
    form = JobPostingForm(instance=job)
    if request.method == 'POST':
        form = JobPostingForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs')
    context = {'form': form}
    return render(request, 'form.html', context=context)


@login_required
@company_required
def delete_job(request, pk):
    job = JobPosting.objects.get(id=pk)
    if request.user.id != job.company.user.id:
        return HttpResponse("Unauthorized Access", 403)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs')
    context = {'item': job}
    return render(request, 'delete.html', context=context)

