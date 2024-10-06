from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from Professionals.models import Professional

# Create your models here.
User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "sent_messages")
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "received_messages")
    content = models.TextField(null = False)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}'