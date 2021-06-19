from django.urls import path
from .views import *

urlpatterns = [
    # project
    path("create", CreateProjectView.as_view()),
    path("list", ProjectListView.as_view()),
    path("<int:pk>", ProjectDetailView.as_view()),
    path("<int:pk>/update", ProjectUpdateView.as_view()),
    path("<int:pk>/delete", ProjectDeleteView.as_view()),
    # task
    path("<int:pk>/task/create", TaskCreateView.as_view()),
    path("<int:pk>/task/list", TaskListView.as_view()),
    path("<int:pk>/task/<int:pk_task>/update", TaskUpdateView.as_view()),
    path("<int:pk>/task/<int:pk_task>/delete", TaskDeleteView.as_view()),
    # subtask
    path(
        "<int:pk>/task/<int:pk_task>/subtask/create",
        SubtaskCreateView.as_view(),
    ),
    path(
        "<int:pk>/task/<int:pk_task>/subtask/list",
        SubtaskListView.as_view(),
    ),
    path(
        "<int:pk>/task/<int:pk_task>/subtask/<int:pk_subtask>/delete",
        SubtaskDeleteView.as_view(),
    ),
    path(
        "<int:pk>/task/<int:pk_task>/subtask/<int:pk_subtask>/update",
        SubtaskUpdateView.as_view(),
    ),
]
