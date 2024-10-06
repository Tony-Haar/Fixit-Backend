from django.urls import path

from . import views


urlpatterns = [
    path("", views.DomainListCreateAPIView.as_view(), name = "domain_list"),
    path("create/", views.DomainListCreateAPIView.as_view(), name = "domain_create"),
    path("<int:pk>/", views.DomainDetailAPIView.as_view(), name = "domain_detail"),
    path("update/<int:pk>/", views.DomainUpdateAPIView.as_view(), name = "domain_update"),
    path("delete/<int:pk>/", views.DomainDestroyAPIView.as_view(), name = "domain_delete"),
    
    path("services/create/", views.ServiceListCreateAPIView.as_view(), name = "service_create"),
    path("services/", views.ServiceListCreateAPIView.as_view(), name = "service_list"),
    path("services/<int:pk>/", views.ServiceDetailAPIView.as_view(), name = "service_detail"),
    path("services/update/<int:pk>/", views.ServiceUpdateAPIView.as_view(), name = "service_update"),
    path("services/delete/<int:pk>/", views.ServiceDestroyAPIView.as_view(), name = "service_delete"),
]