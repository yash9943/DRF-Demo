from django.shortcuts import render
from rest_framework import generics
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsMemberOrOwner, IsTaskOwnerOrMember

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsMemberOrOwner]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsMemberOrOwner]

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsTaskOwnerOrMember]