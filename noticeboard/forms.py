from django.forms import ModelForm
from .models import *
from notifications.utils import send_notifications_to_students_companies


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

    def save(self, commit=True):
        super().save()
        text = self.cleaned_data.get('content')[:40]
        if len(self.cleaned_data.get('content')) > 40:
            text += '...'
        send_notifications_to_students_companies(content='New Announcement: ' + text, url='/announcements')
