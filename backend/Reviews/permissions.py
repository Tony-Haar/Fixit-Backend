from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Assumes the model instance has a `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS allows GET, HEAD or METHOD requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # checking if the authenticated user is the one who created the object
        return obj.user == request.user
    