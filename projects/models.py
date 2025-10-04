from django.db import models
import uuid
from users.models import users
from teams.models import Team

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("planned", "Planned"),
            ("ongoing", "Ongoing"),
            ("completed", "Completed"),
            ("on_hold", "On Hold")
        ],
        default="planned"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name