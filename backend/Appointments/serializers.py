from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Appointment
from Professionals.models import Professional
from ServiceRequest.models import ServiceRequest
from Professionals.serializers import ProfessionalSerializer
from Users.serializers import UserSerializer
from ServiceRequest.serializers import ServiceRequestSerializer


User = get_user_model()

class AppointmentSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(queryset = Professional.objects.all(), write_only = True)
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only = True)
    service_request = serializers.PrimaryKeyRelatedField(queryset = ServiceRequest.objects.all(), write_only = True)
    #professional_details = ProfessionalSerializer(source = "professional", read_only = True)
    #user_details = UserSerializer(source = "user", read_only = True)
    service_request_details = ServiceRequestSerializer(source = "service_request", read_only = True)

    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'professional',
            #'professional_details', #NO NEED TO ADD AS THEY ARE ALREADY IN SERVICE_REQUEST_DETAILS
            'user',
            #'user_details',
            'service_request',
            'service_request_details',
            'date',
            'status',
        ]
