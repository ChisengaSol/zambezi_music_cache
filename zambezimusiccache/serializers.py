from rest_framework import serializers
from .models import *
from user_accounts.models import User

class MusicianSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Musician
        fields = ["id","user","stage_name","image","bio"]
                         