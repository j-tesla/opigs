from django.db import models
from accounts.models import User


class Notification(models.Model):
    users = models.ManyToManyField(to=User)
    url = models.URLField()
    content = models.CharField(max_length=200, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
