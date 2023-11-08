from uuid import UUID

from requests import Request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from userAPI.models import UserDB
from userAPI.serializer import UserSerializer


# health
@api_view(["GET"])
def health(request: Request):
    """health check."""
    return Response({"status": "success OK"}, status=status.HTTP_200_OK)


# Users
class Users(APIView):
    """get all users / create users."""

    def get(self, request: Request):
        """get all users."""
        users = UserDB.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        """create users."""
        serializer = UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_user_active(request: Request):
    """get all users who are active."""
    users = UserDB.objects.filter(active=True)
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_user_not_active(request: Request):
    """get all users who are active."""
    users = UserDB.objects.filter(active=False)
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_user_less_than_age(request: Request, age: int):
    """get all users who's age small than target age."""
    users = UserDB.objects.filter(age__lte=age)
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_user_greater_than_age(request: Request, age: int):
    """get all users who's age small than target age."""
    users = UserDB.objects.filter(age__gte=age)
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# User
class User(APIView):
    """get / update / delete user."""

    def get(self, request: Request, primary_key: UUID):
        """get user by id."""
        try:
            user_db = UserDB.objects.get(pk=primary_key)
        except:
            return Response(
                {"info": f"user with id {primary_key} is not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = UserSerializer(instance=user_db)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, primary_key: UUID):
        """update user by id."""
        try:
            user_db = UserDB.objects.get(pk=primary_key)
        except:
            return Response(
                {"info": f"user with id {primary_key} is not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = UserSerializer(instance=user_db, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, primary_key: UUID):
        """delete user by id."""
        try:
            user_db = UserDB.objects.get(pk=primary_key)
        except:
            return Response(
                {"info": f"user with id {primary_key} is not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        user_db.delete()
        return Response({"delete": user_db.name}, status=status.HTTP_204_NO_CONTENT)
