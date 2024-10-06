from django.contrib import admin
from .models import Domain, Service


# Register your models here.
admin.site.register(Domain)
admin.site.register(Service)