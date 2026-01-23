import django_filters
from .models import Task, Project

class ProjectFilter(django_filters.FilterSet):
    project = django_filters.NumberFilter(field_name='id')
    
    class Meta:
        model = Project
        fields = ['project']

class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter(field_name='completed')
    due_date = django_filters.DateFilter(field_name='due_date')

    class Meta:
        model = Task
        fields = ['completed', 'due_date']
