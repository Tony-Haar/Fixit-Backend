from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User  # Assuming we are using Django's built-in User model

from Professionals.models import Professional
from Domains.models import Domain, Service

# Create your models here.

class ServiceRequest(models.Model):
    class UrgencyChoices(models.TextChoices):
        LOW = 'Low'
        MEDIUM = 'Medium'
        HIGH = 'High'

    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        ACCEPTED = 'Accepted'
        COMPLETED = 'Completed'
        CANCELLED = 'Cancelled'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'service_requests')
    professional = models.ForeignKey(Professional, on_delete = models.CASCADE, related_name = 'service_requests')
    category = models.ForeignKey(Domain, on_delete = models.CASCADE, related_name = 'service_requests')
    service = models.ForeignKey(Service, on_delete = models.CASCADE, related_name ='service_requests')
    description = models.TextField(blank = True, default = '', null = True)
    urgency = models.CharField(max_length = 6, choices = UrgencyChoices.choices)
    status = models.CharField(max_length = 9, choices = StatusChoices.choices)
    budget = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return f'Service Request {self.id} - {self.status}'


    