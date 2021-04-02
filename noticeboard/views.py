from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required


# Create your views here.

@login_required
def get_announcements(request):
    announcements_ = Announcement.objects.all()

    context = {'announcements': announcements_, 'user': request.user}

    return render(request, 'noticeboard/noticeboard.html', context=context)


@login_required
@admin_required
def post_announcement(request):
    form = AnnouncementForm()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    context = {'form': form}
    return render(request, 'noticeboard/announcement_form.html', context=context)


@login_required
@admin_required
def update_announcement(request, pk):
    announcement = Announcement.objects.get(id=pk)
    form = AnnouncementForm(instance=announcement)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    context = {'form': form}
    return render(request, 'noticeboard/announcement_form.html', context=context)


@login_required
@admin_required
def delete_announcement(request, pk):
    announcement = Announcement.objects.get(id=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcements')
    context = {'item': announcement}
    return render(request, 'noticeboard/delete.html', context=context)
