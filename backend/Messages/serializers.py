from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Message
from Professionals.models import Professional
from Users.serializers import UserSerializer


User = get_user_model()

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only = True)
    receiver = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only = True)
    sender_details = UserSerializer(source = "sender", read_only = True)
    receiver_details = UserSerializer(source = "receiver", read_only = True)

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'sender_details',
            'receiver',
            'receiver_details',
            'content',
            'timestamp'
        ]