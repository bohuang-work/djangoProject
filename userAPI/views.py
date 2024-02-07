from requests import Request
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from userAPI.models.computer import ComputerDB
from userAPI.models.job import JobDB
from userAPI.models.office import OfficeDB
from userAPI.models.user import UserDB
from userAPI.serializer import (
    ComputerSerializer,
    JobSerializer,
    OfficeSerializer,
    UserSerializer,
)


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


# Jobs
class Jobs(generics.GenericAPIView):
    queryset = JobDB.objects.all()
    serializer_class = JobSerializer

    def get(self, request, format=None):
        users = JobDB.objects.all()
        serializer = JobSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Job
class Job(generics.GenericAPIView):
    serializer_class = JobSerializer

    def get_object(self, pk):
        try:
            return JobDB.objects.get(pk=pk)
        except JobDB.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = JobSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = JobSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Computers
class Computers(generics.GenericAPIView):
    queryset = ComputerDB.objects.all()
    serializer_class = JobSerializer

    def get(self, request, format=None):
        users = ComputerDB.objects.all()
        serializer = ComputerSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComputerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Computer
class Computer(generics.GenericAPIView):
    serializer_class = ComputerSerializer

    def get_object(self, pk):
        try:
            return ComputerDB.objects.get(pk=pk)
        except ComputerDB.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ComputerSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ComputerSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Offices
class Offices(generics.GenericAPIView):
    queryset = OfficeDB.objects.all()
    serializer_class = OfficeSerializer

    def get(self, request, format=None):
        users = OfficeDB.objects.all()
        serializer = OfficeSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OfficeSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Office
class Office(generics.GenericAPIView):
    serializer_class = OfficeSerializer

    def get_object(self, pk):
        try:
            return OfficeDB.objects.get(pk=pk)
        except OfficeDB.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = OfficeSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = OfficeSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
