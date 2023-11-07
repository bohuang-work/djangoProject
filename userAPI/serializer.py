from rest_framework import serializers

from userAPI.models import UserDB


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDB
        fields = "__all__"
