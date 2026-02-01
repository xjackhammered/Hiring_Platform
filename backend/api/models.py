from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, blank=False, null=False)
    archived = models.BooleanField(default=False)
    posted_at = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey("EmployerProfile", on_delete=models.CASCADE, related_name="jobs")
    location = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["-posted_at"]
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="comments")
    content = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-posted_at"]
        indexes = [
            models.Index(fields = ["job"]),
            models.Index(fields = ["author"]),
        ]
    
    def __str__(self):
        return f"{self.author.username}: {self.content[0:10]}"

class EmployerProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employer_profile")
    company_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username 

class CandidateProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="candidate_profile")
    about = models.TextField()
    cv = models.FileField(blank=True, null=True, upload_to="cvs/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.owner.username


