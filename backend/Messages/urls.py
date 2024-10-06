from django.urls import path

from . import views


urlpatterns = [
    path("", views.MessageListCreateAPIView.as_view(), name = "message_list"),
    path("create/", views.MessageListCreateAPIView.as_view(), name = "message_create"),
    path("<int:pk>/", views.MessageDetailAPIView.as_view(), name = "message_detail"),
    path("inbox/<int:receiver_id>/", views.MessageListAPIView.as_view(), name = "message_by_receiver"),
    path("sent/<int:sender_id>/", views.MessageListAPIView.as_view(), name = "message_by_sender"),
    path("delete/<int:pk>/", views.MessageDestroyAPIView.as_view(), name = "message_delete"),
]