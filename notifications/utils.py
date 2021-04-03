from .models import Notification
from accounts.models import User


def send_notification_to_students(content, url):
    students = User.objects.filter(user_type='STUDENT')
    notification = Notification(content=content, url=url)
    notification.save()
    notification.users.add(*students)


def send_notifications_to_students_companies(content, url):
    students = User.objects.filter(user_type='STUDENT')
    companies = User.objects.filter(user_type='COMPANY')
    notification = Notification(content=content, url=url)
    notification.save()
    notification.users.add(*students, *companies)
