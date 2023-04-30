from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .models import *
from .serializers import *


class MusiciansView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Musician.objects.select_related("user").all()
    # stage_name = request.query
    serializer_class = MusicianSerializer

    # def get_throttles(self):
    #     if self.action == "create":
    #         throttle_classes = [UserRateThrottle]
    #     else:
    #         throttle_classes = []
    #     return [throttle() for throttle in throttle_classes]


class SingleMusicianView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Musician.objects.all()
    # queryset = get_object_or_404(Musician,pk=id)
    serializer_class = MusicianSerializer


class AlbumsView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Album.objects.select_related("musician").all()
    serializer_class = AlbumSerializer


class SingleAlbumView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TracksView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Track.objects.select_related("musician", "album").all()
    serializer_class = TrackSerializer


class SingleTrackView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class ListenersView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Listener.objects.select_related("user").all()
    serializer_class = ListenerSerializer


class SingleListenerView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Listener.objects.all()
    serializer_class = ListenerSerializer


class ListensView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Listens.objects.select_related("listener", "track").all()
    serializer_class = ListensSerializer


class SingleListenView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Listens.objects.all()
    serializer_class = ListensSerializer


class PurchasesView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Purchase.objects.select_related("listener", "track").all()
    serializer_class = PurchaseSerializer


class SinglePurchaseView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PaymentsView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Payments.objects.select_related("purchase", "purchase").all()
    serializer_class = PaymentsSerializer


class SinglePaymentView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


# @api_view()
# @permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])  # throttling for authenticated users
# def secret(request):
#     return Response({"message: Some secret message"})


# @api_view()
# @throttle_classes([AnonRateThrottle])  # throttling for anonymous users
# def throttle_check(request):
#     return Response({"message: Successful"})
