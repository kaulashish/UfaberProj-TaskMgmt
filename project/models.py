from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="Creator of the project"
    )
    name = models.CharField(max_length=225, unique=True, help_text="Name of project")
    description = models.TextField(help_text="Description of project")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date updated")
    duration = models.DurationField(
        help_text="Duration of Project", blank=True, null=True
    )
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"Project: {self.name}"

    def calculate_duration(self):
        today = datetime.utcnow()
        return today - self.created_at.replace(tzinfo=None)


class Task(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, help_text="Project of task"
    )
    name = models.CharField(max_length=225, help_text="Name of task", unique=True)
    description = models.TextField(help_text="Description of task")
    start_date = models.DateField(null=True, help_text="Start date for task")
    end_date = models.DateField(null=True, help_text="Deadline for task")
    assignee = models.ManyToManyField(User, help_text="Assignees for task")

    def __str__(self):
        return f"Task: {self.name}"


class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, help_text="Task of task")
    name = models.CharField(max_length=255, help_text="Name of subtask")
    description = models.TextField(help_text="Description of subtask")
    start_date = models.DateField(null=True, help_text="Start date for subtask")
    end_date = models.DateField(null=True, help_text="Deadline for subtask")
    assignee = models.ManyToManyField(User, help_text="Assignees for subtask")

    def __str__(self):
        return f"Subtask: {self.name}"
