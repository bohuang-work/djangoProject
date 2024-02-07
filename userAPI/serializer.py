from rest_framework import serializers

from userAPI.models.computer import ComputerDB
from userAPI.models.job import JobDB
from userAPI.models.office import OfficeDB
from userAPI.models.user import UserDB


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDB
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDB
        fields = "__all__"


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerDB
        fields = "__all__"


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeDB
        fields = "__all__"
