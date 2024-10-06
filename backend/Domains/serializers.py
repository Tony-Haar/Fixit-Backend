from rest_framework import serializers

from .models import Domain, Service


class DomainSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = Domain
        fields = [
            'id', 
            'domain_name'
        ]

class ServiceSerializer(serializers.ModelSerializer):
    domain = serializers.PrimaryKeyRelatedField(queryset = Domain.objects.all(), write_only = True) 
    domain_details = DomainSerializer(source = "domain", read_only = True)

    id = serializers.IntegerField(read_only = True)
    
    class Meta:
        model = Service
        fields = [
            'id',
            'domain',
            'domain_details',
            'service_name',
        ]