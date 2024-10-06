from django.urls import path

from . import views


urlpatterns = [
    path("", views.ReviewListeCreateAPIView.as_view(), name = "review_list"),
    path("create/", views.ReviewListeCreateAPIView.as_view(), name = "review_create"),
    path("<int:pk>/", views.ReviewDetailAPIView.as_view(), name = "review_detail"),
    path("professional/<int:professional_id>/", views.ReviewListAPIView.as_view(), name = "review_professional_detail"),
    path("update/<int:pk>/", views.ReviewUpdateAPIView.as_view(), name = "review_update"),
    path("delete/<int:pk>/", views.ReviewDestroyAPIView.as_view(), name = "review_delete"),
]