from django.forms import ModelForm
from .models import *


class JobPostingForm(ModelForm):
    class Meta:
        model = JobPosting
        fields = '__all__'
