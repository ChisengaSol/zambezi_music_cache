from rest_framework import generics, permissions
from .models import User
from .serializers import UsersSerializer, RegisterSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class SingleUserView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


# Register API
class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UsersSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class Login(KnoxLoginView):  # check one of saved bookmarks for login in django
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(Login, self).post(request, format=None)
