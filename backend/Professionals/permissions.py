from rest_framework import permissions
from .models import Professional


class IsProfessional(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is a professional
        return Professional.objects.filter(user_id = request.user.id).exists()
        

        