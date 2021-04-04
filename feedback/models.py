from django.db import models
from ..accounts.models import Alumni, Company

# Create your models here.
class Feedback(models.Model):
    alumnus = models.ForeignKey(Alumni)
    company = models.ForeignKey(Company)
    content = models.TextField()
