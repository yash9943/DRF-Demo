from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
    
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    details = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='created_tasks')
    
    def __str__(self):
        return self.title
    
    def is_due_within_24_hours(self):
        if not self.due_date:
            return False

        today = timezone.now().date()
        tomorrow = today + timedelta(days=1)

        return today <= self.due_date <= tomorrow