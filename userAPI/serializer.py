from rest_framework import serializers

from userAPI.models.job import JobDB
from userAPI.models.user import UserDB


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDB
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDB
        fields = "__all__"
