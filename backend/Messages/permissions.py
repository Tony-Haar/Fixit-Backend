from rest_framework import permissions


class IsSenderOrReceiver(permissions.BasePermission):

    """ 
    to allow access only to sender or receiver
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user
    

class IsSender(permissions.BasePermission):

    """ 
    to allow access only to sender 
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user

    
class IsReceiver(permissions.BasePermission):

    """ 
    to allow access only to receiver
    """

    def has_object_permission(self, request, view, obj):
        return obj.receiver == request.user
