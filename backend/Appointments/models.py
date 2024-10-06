from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from Professionals.models import Professional
from ServiceRequest.models import ServiceRequest


User = get_user_model()

class Appointment(models.Model):
    class StatusChoices(models.TextChoices):
        SCHEDULED = 'Scheduled', 'Scheduled'
        COMPLETED = 'Completed', 'Completed'
        CANCELLED = 'Cancelled', 'Cancelled'
        
    professional = models.ForeignKey(Professional, on_delete = models.CASCADE, related_name = 'appointments')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'appointments')
    service_request = models.ForeignKey(ServiceRequest, on_delete = models.CASCADE, related_name = 'appointments')
    date = models.DateField(auto_now_add = True)# actually should be datetime note only date
    status = models.CharField(max_length = 9, choices = StatusChoices.choices, default = StatusChoices.SCHEDULED)

    def __str__(self):
        return f"user:{self.user.username} - professional:{self.professional} on {self.date}"