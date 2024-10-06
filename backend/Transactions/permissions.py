from rest_framework import permissions


class IsInvolveInTransaction(permissions.BasePermission):
    """ 
    Permission to both users involved in a transaction: payor and payee
    """

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user or obj.professional.user == request.user)


class IsPayor(permissions.BasePermission):
    """ 
    permission for the user that payed for a service transaction
    as a payor
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    

class IsPayee(permissions.BasePermission):
    """ 
    permission for the professional that received the payment for a service transaction
    as a payee
    """

    def has_object_permission(self, request, view, obj):
        return obj.professional.user == request.user