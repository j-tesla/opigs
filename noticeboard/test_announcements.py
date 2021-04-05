import pytest
from .models import Announcement
from django.utils import timezone

@pytest.mark.django_db
def test_announcements():
    date = timezone.now()
    announcement = Announcement(date_posted=date,content="Placements start from tomorrow!!")

    assert announcement.date_posted==date
    assert announcement.content=='Placements start from tomorrow!!'