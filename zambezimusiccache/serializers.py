from rest_framework import serializers
from .models import *
from user_accounts.models import User

class MusicianSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Musician
        fields = ["id","user","stage_name","image","bio"]

                         
class AlbumSerializer(serializers.ModelSerializer):
    musician = serializers.StringRelatedField()
    class Meta:
        model = Album
        fields = ["id","title","musician","price","image","description","release_date"]

class TrackSerializer(serializers.ModelSerializer):
    musician = serializers.StringRelatedField()
    album = serializers.StringRelatedField()
    class Meta:
        model = Track
        fields = ["id","musician","title","image","description","file","album","price","is_available","release_date"]
    

class ListenerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Listener
        fields = ["id","user","balance"]

class ListensSerializer(serializers.ModelSerializer):
    listener = serializers.StringRelatedField()
    track = serializers.StringRelatedField()
    class Meta:
        model = Listens
        fields = ["id","listener","track","listen_date"]

class PurchaseSerializer(serializers.ModelSerializer):
    listener = serializers.StringRelatedField()
    track = serializers.StringRelatedField()
    class Meta:
        model = Purchase
        fields = ["id","listener","track","purchase_date","amount"]

class PaymentsSerializer(serializers.ModelSerializer):
    listener = serializers.StringRelatedField()
    purchase = serializers.StringRelatedField()
    class Meta:
        model = Payments
        fields = ["id","listener","purchase","payment_date","amount"]