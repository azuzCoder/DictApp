from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView,
                            generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
