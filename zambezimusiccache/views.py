from rest_framework import generics
from .models import *
from .serializers import *

class MusiciansView(generics.ListCreateAPIView):
    queryset = Musician.objects.select_related('user').all()
    serializer_class = MusicianSerializer

class SingleMusicianView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Musician.objects.all()
    #queryset = get_object_or_404(Musician,pk=id)
    serializer_class = MusicianSerializer




