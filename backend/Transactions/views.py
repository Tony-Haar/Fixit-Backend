from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from Transactions.models import Transaction
from .serializers import TransactionSerializer
from .permissions import IsInvolveInTransaction, IsPayor, IsPayee


# Transaction views
class TransactionListeCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

class TransactionDetailAPIView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsInvolveInTransaction]

class TransactionListAPIView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        if "user_id" in self.kwargs:
            user_id = self.kwargs["user_id"]
            return Transaction.objects.filter(user_id = user_id)
        elif "professional_id" in self.kwargs:
            professional_id = self.kwargs["professional_id"]
            return Transaction.objects.filter(professional_id = professional_id)
        
    def get_permissions(self):
        if "user_id" in self.kwargs:
            permission_classes = [permissions.IsAuthenticated, IsPayor]
        elif "professional_id" in self.kwargs:
            permission_classes = [permissions.IsAuthenticated, IsPayee]
        return [permission() for permission in permission_classes]
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for obj in queryset:
            self.check_object_permissions(request, obj)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
