from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view(), name = "user_register"),
    path('login/', views.UserLoginAPIView.as_view(), name = 'user_login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name = 'user_logout'),
    path('', views.UserListAPIView.as_view(), name = 'user_list'),
    path('<int:pk>/', views.UserDetailAPIView.as_view(), name = 'user_detail'),
    path('update/<int:pk>/', views.UserUpdateAPIView.as_view(), name = 'user_update'),
    path('delete/<int:pk>/', views.UserDestroyAPIView.as_view(), name = 'user_update'),
]