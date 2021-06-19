from django.contrib import admin
from .models import *

# Register your models here.
class TaskInline(admin.StackedInline):
    model = Task


class SubtaskInline(admin.StackedInline):
    model = SubTask


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

    class Meta:
        model = Project


class TaskAdmin(admin.ModelAdmin):
    inlines = [SubtaskInline]

    class Meta:
        model = Task


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask)
