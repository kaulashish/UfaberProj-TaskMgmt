from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework import status, generics
from django.db.utils import IntegrityError

# Create your views here.


class CreateProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = get_object_or_404(User, username=request.user)
            name = request.data.get("name")
            description = request.data.get("description")
            image = request.data.get("image")

            proj_obj = Project.objects.create(
                user=user,
                name=name,
                description=description,
                image=image,
            )

            proj_obj.duration = proj_obj.calculate_duration()
            proj_obj.save()

            return Response(
                {
                    "status": "Success",
                    "detail": "Project created",
                    "data": ProjectSerializer(proj_obj).data,
                },
                status=status.HTTP_201_CREATED,
            )
        except IntegrityError:
            return Response(
                {"error": "Project name already exists"},
                status=status.HTTP_201_CREATED,
            )


class ProjectListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = get_object_or_404(User, username=request.user)
        project_objects = user.project_set.all()
        for project_obj in project_objects:
            project_obj.duration = project_obj.calculate_duration()
            project_obj.save()
        serializer_obj = ProjectSerializer(project_objects, many=True)
        return Response({"data": serializer_obj.data}, status=status.HTTP_200_OK)


class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer


class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    lookup_field = "pk"
    queryset = Project.objects.all()


class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            proj_obj = Project.objects.get(id=pk)

            name = request.data.get("name")
            description = request.data.get("description")
            start_date = request.data.get("start_date")
            end_date = request.data.get("end_date")
            assignee = request.data.getlist("assignee")

            task_obj = Task.objects.create(
                project=proj_obj,
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
            )

            for assignee in assignee:
                assignee_obj = User.objects.get(username=assignee)
                task_obj.assignee.add(assignee_obj)

            return Response(
                {"detail": "Task created", "data": TaskSerializer(task_obj).data},
                status=status.HTTP_201_CREATED,
            )
        except IntegrityError:
            return Response(
                {"error": "Task already exists"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )


class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        project_obj = Project.objects.get(id=pk)
        queryset = project_obj.task_set.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, pk_task):
        task_obj = get_object_or_404(Task, id=pk_task)
        task_obj.delete()
        return Response(
            {"detail": "Task deleted successfully"}, status=status.HTTP_200_OK
        )


class TaskUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, pk_task):
        task_obj = Task.objects.get(id=pk_task)

        name = request.data.get("name")
        description = request.data.get("description")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")

        serializer = TaskSerializer(task_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            serializer.errors

        for assignee in request.data.getlist("assignee"):
            user_obj = get_object_or_404(User, username=assignee)
            if user_obj in task_obj.assignee.all():
                task_obj.assignee.remove(user_obj)
            else:
                task_obj.assignee.add(user_obj)

        return Response(
            {"detail": "Task updated", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


class SubtaskCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, pk_task):
        try:
            project = Project.objects.get(id=pk)
            task_obj = Task.objects.get(id=pk_task)

            name = request.data.get("name")
            description = request.data.get("description")
            start_date = request.data.get("start_date")
            end_date = request.data.get("end_date")
            assignee = request.data.getlist("assignee")

            subtask_obj = SubTask.objects.create(
                task=task_obj,
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
            )

            for assignee in assignee:
                assignee_obj = get_object_or_404(User, username=assignee)
                if assignee_obj in task_obj.assignee.all():
                    subtask_obj.assignee.add(assignee_obj)
                else:
                    return Response(
                        {
                            "error": f"User with username '{assignee}' not in Task assignee"
                        },
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    )

            return Response(
                {
                    "detail": "Sub-Task created",
                    "data": SubTaskSerializer(subtask_obj).data,
                },
                status=status.HTTP_201_CREATED,
            )
        except IntegrityError:
            return Response(
                {"error": "Sub-Task already exists"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )


class SubtaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, pk_task):
        task_obj = Task.objects.get(id=pk_task)
        queryset = task_obj.subtask_set.all()
        serializer = SubTaskSerializer(queryset, many=True)
        return Response(serializer.data)


class SubtaskDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, pk_task, pk_subtask):
        subtask_obj = get_object_or_404(SubTask, id=pk_subtask)
        subtask_obj.delete()
        return Response(
            {"detail": "Task deleted successfully"}, status=status.HTTP_200_OK
        )


class SubtaskUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, pk_task, pk_subtask):
        subtask_obj = SubTask.objects.get(id=pk_subtask)
        task_obj = subtask_obj.task
        name = request.data.get("name")
        description = request.data.get("description")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")

        serializer = SubTaskSerializer(subtask_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            serializer.errors

        for assignee in request.data.getlist("assignee"):
            user_obj = get_object_or_404(User, username=assignee)
            if user_obj in task_obj.assignee.all():
                if user_obj in subtask_obj.assignee.all():
                    subtask_obj.assignee.remove(user_obj)
                else:
                    subtask_obj.assignee.add(user_obj)
            else:
                return Response(
                    {"error": f"User with username '{assignee}' not in Task assignee"},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                )

        return Response(
            {"detail": "Sub-Task updated", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
