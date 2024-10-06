from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import ServiceRequest
from Professionals.models import Professional
from Domains.models import Domain, Service
from Users.serializers import UserSerializer
from Professionals.serializers import ProfessionalSerializer
from Domains.serializers import DomainSerializer, ServiceSerializer


User = get_user_model()

class ServiceRequestSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(queryset = Professional.objects.all(), write_only = True)
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only = True)
    category = serializers.PrimaryKeyRelatedField(queryset = Domain.objects.all(), write_only = True)
    service = serializers.PrimaryKeyRelatedField(queryset = Service.objects.all(), write_only = True)
    user_details = UserSerializer(source = "user", read_only = True)
    professional_details = ProfessionalSerializer(source = "professional", read_only = True)
    domain_details = DomainSerializer(source = "category", read_only = True)
    service_details = ServiceSerializer(source = "service", read_only = True)

    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = ServiceRequest
        fields = [
            'id',
            'user',
            'user_details',
            'professional',
            'professional_details',
            'category',
            'domain_details',
            'service',
            'service_details',
            'description',
            'urgency',
            'status',
            'budget',
        ]
