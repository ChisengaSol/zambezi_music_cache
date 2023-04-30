from django.urls import path
from . import views

# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("musicians/", views.MusiciansView.as_view()),
    path("musicians/<int:pk>", views.SingleMusicianView.as_view()),
    path("albums/", views.AlbumsView.as_view()),
    path("albums/<int:pk>", views.SingleAlbumView.as_view()),
    path("tracks/", views.TracksView.as_view()),
    path("tracks/<int:pk>", views.SingleTrackView.as_view()),
    path("listeners/", views.ListenersView.as_view()),
    path("listeners/<int:pk>", views.SingleListenerView.as_view()),
    path("listens/", views.ListensView.as_view()),
    path("listens/<int:pk>", views.SingleListenView.as_view()),
    path("purchases/", views.PurchasesView.as_view()),
    path("purchases/<int:pk>", views.SinglePurchaseView.as_view()),
    path("payments/", views.PaymentsView.as_view()),
    path("payments/<int:pk>", views.SinglePaymentView.as_view()),
    # path("secret/", views.secret),
    # path("api-token-auth/", obtain_auth_token),
    # path("throttle-check/", views.throttle_check),
]
