from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    archived = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)