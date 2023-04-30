from knox import views as knox_views
from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<int:pk>", views.SingleUserView.as_view()),
    path("register/", views.Register.as_view()),
    path("login/", views.Login.as_view()),
    path("logout/", knox_views.LogoutView.as_view()),
    path("logoutall/", knox_views.LogoutAllView.as_view()),
]
