from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, authentication, permissions

from .models import Appointment
from .serializers import AppointmentSerializer
from Reviews.permissions import IsOwnerOrReadOnly


# Appointment views
""" 
in case i'm running into any incomprehension:
check the matching of service request user and professional 
and appointment user and professional
"""
class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class AppointmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class AppointmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
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
    
class AppointmentDestroyAPIView(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

