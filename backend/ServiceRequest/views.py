from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, authentication, permissions

from .models import ServiceRequest
from .serializers import ServiceRequestSerializer
from Reviews.permissions import IsOwnerOrReadOnly


# service request views
class ServiceRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ServiceRequestDetailAPIView(generics.RetrieveAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ServiceRequestUpdateAPIView(generics.UpdateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ServiceRequestDestroyAPIView(generics.DestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
