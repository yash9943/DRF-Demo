from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import User

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        superuser = User.objects.filter(id=request.user.id, is_superuser=True)
        return superuser
    
class IsMemberOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser: 
            return True
        if request.method in SAFE_METHODS:
            return (obj.owner.pk == user.pk 
                    or user in obj.members.all())
        else:
            return obj.owner.pk == user.pk

class IsTaskOwnerOrMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_superuser:
            return True
        if user == obj.created_by:
            return True
        if request.method in SAFE_METHODS:
            return (obj.project.owner.pk == user.pk or 
                    user in obj.project.members.all())
        else:
            return obj.project.owner.pk == user.pk
        