from django.forms import ModelForm
from .models import *


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'
