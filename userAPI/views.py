from django_q.tasks import schedule
from requests import Request
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from userAPI.models import UserDB
from userAPI.serializer import UserSerializer
from userAPI.tasks import get_all_users


# health
@api_view(["GET"])
def health(request: Request):
    """health check."""
    return Response({"status": "success OK"}, status=status.HTTP_200_OK)


# Users
class Users(generics.GenericAPIView):
    queryset = UserDB.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        users = UserDB.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User
class User(generics.GenericAPIView):
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return UserDB.objects.get(pk=pk)
        except UserDB.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
