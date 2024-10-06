from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Transaction
from Professionals.models import Professional
from Professionals.serializers import ProfessionalSerializer
from Users.serializers import UserSerializer


User = get_user_model()

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only = True)
    professional = serializers.PrimaryKeyRelatedField(queryset = Professional.objects.all(), write_only = True)
    user_details = UserSerializer(source = "user", read_only = True)
    professional_details = ProfessionalSerializer(source = "professional", read_only = True)

    class Meta:
        model = Transaction 
        fields = [
            'id',
            'user',
            'user_details',
            'professional',
            'professional_details',
            'amount',
            'timestamp',
            'currency'
        ]
        
