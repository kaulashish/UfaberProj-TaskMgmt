from rest_framework import serializers
from .models import *
from user.serializers import *


class SubTaskSerializer(serializers.ModelSerializer):
    assignee = UserSerializer(many=True, read_only=True)

    class Meta:
        model = SubTask
        fields = [
            "id",
            "task",
            "name",
            "description",
            "start_date",
            "end_date",
            "assignee",
        ]


class TaskSerializer(serializers.ModelSerializer):
    subtask = SubTaskSerializer(source="subtask_set", many=True, read_only=True)
    assignee = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "project",
            "name",
            "description",
            "start_date",
            "end_date",
            "assignee",
            "subtask",
        ]


class ProjectSerializer(serializers.ModelSerializer):
    task = TaskSerializer(source="task_set", many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "user",
            "name",
            "description",
            "created_at",
            "updated_at",
            "duration",
            "image",
            "task",
        ]
