from django.db import models

# Create your models here.

class Domain(models.Model):
    domain_name = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return self.domain_name

class Service(models.Model):
    domain = models.ForeignKey(Domain, on_delete = models.CASCADE, related_name = "services")
    service_name = models.CharField(max_length = 300, null = False, blank = False, default = "None")

    def __str__(self):
        return f"{self.domain.domain_name} - {self.service_name}"