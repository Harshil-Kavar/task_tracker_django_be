from django.db import models
import uuid

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('review', 'In Review'),
        ('done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    module = models.ForeignKey("project_modules.Module", on_delete=models.CASCADE, related_name="tasks")
    assigned_to_user = models.ForeignKey("users.users", on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")  
    assigned_to_team = models.ForeignKey("teams.Team", on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title