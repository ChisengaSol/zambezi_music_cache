from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<int:pk>", views.SingleUserView.as_view()),
    path('register/', views.RegisterAPI.as_view()),
]
