from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Professional, Profile, ExperienceBackground
from Domains.models import Domain
from Domains.serializers import DomainSerializer
from Users.serializers import UserSerializer


User = get_user_model()

class ProfessionalSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only = True)
    domain = serializers.PrimaryKeyRelatedField(queryset = Domain.objects.all(), write_only = True)
    user_details = UserSerializer(source = "user", read_only = True)
    domain_details = DomainSerializer(source = "domain", read_only = True)

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Professional 
        fields = [
            'id',
            'user',
            'domain',
            'user_details',
            'domain_details',
            'photo',
            'availability', 
            'rating', 
        ]

class ProfileSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(queryset = Professional.objects.all(), write_only = True)
    professional_details = ProfessionalSerializer(source = "professional", read_only = True)
    
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile 
        fields = [
            'id',
            'professional',
            'professional_details',
            'about',
            'title',
            'year_of_experience',
        ]

class ExperienceBackgroundSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset = Profile.objects.all(), write_only = True)
    profile_details = ProfileSerializer(source = "profile", read_only = True)
    
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ExperienceBackground
        fields = [
            'id',
            'profile',
            'profile_details',
            'worked_at',
            'duration',
            'title',
            'assigned_work',
        ]


