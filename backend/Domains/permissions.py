from rest_framework import permissions


class IsAuthenticatedOrAdminUser(permissions.BasePermission):

    """ 
    create and list endpoint:
    allow authenticated user for listing
    allow only AdminUser for creating
    """

    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user and request.user.is_authenticated
        elif request.method == "POST":
            return request.user and request.user.is_staff
        return False
