from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('professionals/', include('Professionals.urls')),
    path('domains/', include('Domains.urls')),
    path('servicerequests/', include('ServiceRequest.urls')),
    path('users/', include('Users.urls')),
    path('appointments/', include('Appointments.urls')),
    path('transactions/', include('Transactions.urls')),
    path('reviews/', include('Reviews.urls')),
    path('messages/', include('Messages.urls')),
]
