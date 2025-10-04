from django.db import models
import uuid
from projects.models import Project

# Create your models here.
class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="modules")
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("in_progress", "In Progress"),
            ("done", "Done")
        ],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name