from django.db import models
from accounts.models import Alumni, Company

# Create your models here.
class Feedback(models.Model):
    alumnus = models.ForeignKey(Alumni, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
