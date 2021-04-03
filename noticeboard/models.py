from django.db import models


# Create your models here.

class Announcement(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        text = self.content[:40]
        if len(self.content) > 40:
            text += '...'
        return text
