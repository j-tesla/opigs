from django.db import models


# Create your models here.

class Announcement(models.Model):
    date_posted = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=500)

    def __str__(self):
        text = self.content[:60]
        if len(self.content) > 60:
            text += '...'
        return text
