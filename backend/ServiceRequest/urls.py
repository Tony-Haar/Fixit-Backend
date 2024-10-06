from django.urls import path

from . import views



urlpatterns = [
    path("create/", views.ServiceRequestListCreateAPIView.as_view(), name = "service_request_create"),
    path("", views.ServiceRequestListCreateAPIView.as_view(), name = "service_request_list"),
    path("<int:pk>/", views.ServiceRequestDetailAPIView.as_view(), name = "service_request_detail"),
    path("update/<int:pk>/", views.ServiceRequestUpdateAPIView.as_view(), name = "service_request_update"),
    path("delete/<int:pk>/", views.ServiceRequestDestroyAPIView.as_view(), name = "service_request_delete"),
]