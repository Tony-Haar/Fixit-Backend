from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """ 
    permission allowed to the owner of user data
    """

    def has_object_permission(self, request, view, obj):
        return str(obj.email) == str(request.user)


class IsOwnerOrAdminUser(permissions.BasePermission):
    """ 
    permission allowed to the owner of user data or adminUser
    """

    def has_object_permission(self, request, view, obj):
        return str(obj.email) == str(request.user) or request.user.is_staff