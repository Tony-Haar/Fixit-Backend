from django.urls import path 

from . import views


urlpatterns = [
    path("create/", views.TransactionListeCreateAPIView.as_view(), name = "transaction_create"),
    path("", views.TransactionListeCreateAPIView.as_view(), name = "transaction_list"),
    path("<int:pk>/", views.TransactionDetailAPIView.as_view(), name = "transaction_detail"),
    path("user/<int:user_id>/", views.TransactionListAPIView.as_view(), name = "transaction_user_detail"),
    path("professional/<int:professional_id>/", views.TransactionListAPIView.as_view(), name = "transaction_professional_detail"),
]