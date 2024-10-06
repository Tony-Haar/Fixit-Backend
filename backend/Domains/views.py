from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, authentication, permissions

from .models import Domain, Service
from .serializers import DomainSerializer, ServiceSerializer
from .permissions import IsAuthenticatedOrAdminUser


# Domain views
class DomainListCreateAPIView(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsAuthenticatedOrAdminUser]

class DomainDetailAPIView(generics.RetrieveAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class DomainUpdateAPIView(generics.UpdateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DomainDestroyAPIView(generics.DestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]


# Service views
class ServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsAuthenticatedOrAdminUser]

class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ServiceUpdateAPIView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data, partial = partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ServiceDestroyAPIView(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
