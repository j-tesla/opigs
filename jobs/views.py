from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import JobPosting
from .forms import JobPostingForm
from accounts.decorators import verified_company_required, student_required
from accounts.models import Company, Student
from notifications.models import Notification


@login_required
def get_jobs(request):
    jobs = JobPosting.objects.all()

    context = {"joblist": jobs}

    return render(request, 'jobs/jobs.html', context=context)


@login_required
@verified_company_required
def post_job(request):
    form = JobPostingForm()
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        Company.objects.get(user__id=request.user.id)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = Company.objects.get(user__id=request.user.id)
            job.save()
            return redirect('jobs')
    context = {'form': form}
    return render(request, 'form.html', context=context)


@login_required
@verified_company_required
def update_job(request, pk):
    job = JobPosting.objects.get(id=pk)
    if request.user.id != job.company.user.id:
        return HttpResponse("Unauthorized Access", 403)
    if request.method == 'POST':
        form = JobPostingForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs')
    form = JobPostingForm(instance=job)
    context = {'form': form}
    return render(request, 'form.html', context=context)


@login_required
@verified_company_required
def delete_job(request, pk):
    job = JobPosting.objects.get(id=pk)
    if request.user.id != job.company.user.id:
        return HttpResponse("Unauthorized Access", 403)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs')
    context = {'item': job}
    return render(request, 'delete.html', context=context)


@login_required
@student_required
def apply_to_job(request, pk):
    job = JobPosting.objects.get(id=pk)
    student = Student.objects.get(user__id=request.user.id)
    if request.method == 'POST':
        if job.applicants.filter(user__id=request.user.id).count():
            return redirect('job', pk)
        job.applicants.add(student)
        notification = Notification(content='New Applicant: ' + student.user.name, url=f'/profile/{request.user.id}')
        notification.users.add(job.company)
        notification.save()

    return redirect('job', pk)


@login_required
def get_job(request, pk):
    job = JobPosting.objects.get(id=pk)
    context = {'job': job, 'user': request.user}
    return render(request, 'jobs/job.html', context=context)
