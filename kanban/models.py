from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=32)

class Ticket(models.Model):
    """
    A ticket has a name, a description and a status which indicates where the ticket is in the current workflow.

    A ticket must always be part of a project.
    """
    STATUS_CHOICES = {
            "TD": "To Do",
            "IP": "In Progress",
            "FI": "Done",
            "OH": "On Hold"
            }
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ticket')
    name = models.CharField(max_length=32)
    description = models.CharField()
    status = models.CharField(
            max_length=2,
            choices=STATUS_CHOICES,
            default="TD",
            )
    assignee = models.ForeignKey(
            User,
            on_delete=models.SET_NULL,
            blank=True,
            null=True,
            )

