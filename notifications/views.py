from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import Notification


@login_required
def get_notifications(request):
    user = User.objects.get(id=request.user.id)
    notifications = user.notification_set.all()
    context = {'notifications': notifications}
    return render(request, 'notifications/notifications.html', context=context)


@login_required
def delete_notification(request, pk):
    if request.method == 'POST':
        print(f"POST {pk}")
        user = User.objects.get(id = request.user.id)
        notification = Notification.objects.get(id=pk)
        user.notification_set.remove(notification)
    return redirect('notifications')


@login_required
def clear_notifications(request):
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        user.notification_set.clear()
    return redirect('notifications')
