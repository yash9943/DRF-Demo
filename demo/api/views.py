from django.shortcuts import render
from rest_framework import generics
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsMemberOrOwner, IsTaskOwnerOrMember, IsSuperUser
from .filters import TaskFilter, ProjectFilter

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = [IsSuperUser]


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsMemberOrOwner]
    filterset_class = ProjectFilter
    filterset_fields = ['project']
    
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
    filterset_class = TaskFilter
    filterset_fields = ['completed', 'due_date']


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsTaskOwnerOrMember]
    
class ComplateTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsTaskOwnerOrMember]
    
    def perform_update(self, serializer):
        serializer.save(completed=True)