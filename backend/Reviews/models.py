from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
#from django.utils import timezone

from Professionals.models import Professional

# Create your models here.
User = get_user_model()

def validate_rating(value): # use for  business rules constraints e.g age constraints,pwd constraint, discount constraint, username uniqueness
    if value < 1 or value > 5:
        raise ValidationError(
            "%(value)s is not between 1 and 5",
            params = {"value": value} # The params dictionary is used to map the placeholders in the message string to the actual values
        )

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "reviews")
    professional = models.ForeignKey(Professional, on_delete = models.CASCADE, related_name = "reviews")
    rating = models.IntegerField(validators = [validate_rating])
    comment = models.TextField(blank = True, null = True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'Review {self.id}: Rating {self.rating}'
