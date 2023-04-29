from django.urls import path
from . import views

urlpatterns = [
    path('musicians/',views.MusiciansView.as_view()),
    path('musicians/<int:pk>',views.SingleMusicianView.as_view()),
]