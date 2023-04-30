from rest_framework import generics
from .models import User
from .serializers import UsersSerializer, RegisterSerializer
from rest_framework.response import Response
from knox.models import AuthToken

class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

class SingleUserView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UsersSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })