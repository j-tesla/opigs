from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User


@login_required
def get_notifications(request):
    user = User.objects.get(id=request.user.id)
    notifications = user.notification_set.all()
    context = {'notifications': notifications}
    return render(request, 'notifications/notifications.html', context=context)


@login_required
def delete_notification(request, pk):
    user = User.objects.get(request.id)
    user.notification_set.remove(id=pk)
    return redirect('notifications')
    # todo method post


def clear_notifications(request):
    user = User.objects.get(request.id)
    user.notification_set.clear()
    # todo method post
