from rest_framework import serializers
from .models import User


# User Serializer
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "date_joined", "is_musician"]


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "date_joined", "is_musician", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            date_joined=validated_data["date_joined"],
            is_musician=validated_data["is_musician"],
            password=validated_data["password"],
        )

        return user
