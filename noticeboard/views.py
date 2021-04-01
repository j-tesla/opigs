from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

def get_announcements(request):
    announcements_ = Announcement.objects.all()

    context = {'announcements': announcements_}

    return render(request, 'noticeboard/noticeboard.html', context=context)


def post_announcement(request):
    form = AnnouncementForm()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcements')
    context = {'form': form}
    return render(request, 'noticeboard/announcement_form.html', context=context)


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


def delete_announcement(request, pk):
    announcement = Announcement.objects.get(id=pk)
    if request.method == 'POST':
        announcement.delete()
        redirect('announcements')
    context = {'item': announcement}
    return render(request, 'noticeboard/delete.html', context=context)
