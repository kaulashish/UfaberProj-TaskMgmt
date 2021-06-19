from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.


class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {
                "token": token.key,
                "username": serializer.instance.username,
                "first_name": serializer.instance.first_name,
                "last_name": serializer.instance.last_name,
            },
            status=status.HTTP_201_CREATED,
        )


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        print(username, password)

        if not username or not password:
            return Response(
                {"error": "username or password not provided"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        user_obj = authenticate(username=username, password=password)

        if not user_obj:
            return Response(
                {"error": "username or password is incorrect"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        token, _ = Token.objects.get_or_create(user=user_obj)

        return Response(
            {
                "detail": "Login Successfull",
                "token": token.key,
            },
            status=status.HTTP_200_OK,
        )
