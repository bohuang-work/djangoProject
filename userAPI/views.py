from requests import Request
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from userAPI.models import UserDB
from userAPI.serializer import UserSerializer


# health
@api_view(["GET"])
def health(request: Request):
    """health check."""
    return Response({"status": "success OK"}, status=status.HTTP_200_OK)


class UserList(generics.ListCreateAPIView):
    queryset = UserDB.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDB.objects.all()
    serializer_class = UserSerializer
