from rest_framework import serializers
from .models import Project, Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at', 'owner', 'members']
        
class TaskSerializer(serializers.ModelSerializer):
    due_within_24_hours = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = ['id', 'project', 'title', 'details', 'due_date', 'completed', 'created_at','due_within_24_hours']
        
    def get_due_within_24_hours(self, obj):
        return obj.is_due_within_24_hours()