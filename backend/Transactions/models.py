from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from Professionals.models import Professional


User = get_user_model()

# Create your models here.

class Transaction(models.Model):
    CURRENCY_CHOICES = [
        ("CFA", "Franc CFA"),
        ("USD", "Dollar"),
        ("EUR", "Euro"),
        ("Rps", "Roupies"),
        ("GBP", "Pound sterling"),
    ]

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "transactions")
    professional = models.ForeignKey(Professional, on_delete = models.CASCADE, related_name = "transactions")
    amount = models.DecimalField(max_digits = 7, decimal_places = 2, blank = False, null = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)
    currency = models.CharField(max_length = 16, choices = CURRENCY_CHOICES, default = "USD")

    def __str__(self):
        return f"transaction No: {self.user.id}-{self.id}-{self.professional.id}"