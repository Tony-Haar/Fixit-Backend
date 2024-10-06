from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.AppointmentListCreateAPIView.as_view(), name = "appointment_create"),
    path("", views.AppointmentListCreateAPIView.as_view(), name = "appointment_list"),
    path("<int:pk>/", views.AppointmentDetailAPIView.as_view(), name = "appointment_detail"),
    path("update/<int:pk>/", views.AppointmentUpdateAPIView.as_view(), name = "appointment_update"),
    path("delete/<int:pk>/", views.AppointmentDestroyAPIView.as_view(), name = "appointment_delete"),
]