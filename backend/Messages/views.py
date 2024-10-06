from rest_framework import generics, authentication, permissions
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer
from .permissions import IsSenderOrReceiver, IsSender, IsReceiver


# Message views
class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class MessageDetailAPIView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSenderOrReceiver]

class MessageListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        if "sender_id" in self.kwargs:
            sender_id = self.kwargs["sender_id"]
            return Message.objects.filter(sender_id = sender_id)
        if "receiver_id" in self.kwargs:
            receiver_id = self.kwargs["receiver_id"]
            return Message.objects.filter(receiver_id = receiver_id)
        
    def get_permissions(self):
        if "sender_id" in self.kwargs:
            permission_classes = [permissions.IsAuthenticated, IsSender]
        elif "receiver_id" in self.kwargs:
            permission_classes = [permissions.IsAuthenticated, IsReceiver]
        return [permission() for permission in permission_classes]
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for obj in queryset:
            self.check_object_permissions(request, obj)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
class MessageDestroyAPIView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsSender]

