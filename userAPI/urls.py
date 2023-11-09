from django.urls import path

from userAPI.models import UserDB
from userAPI.views import (
    User,
    Users,
    get_user_active,
    get_user_greater_than_age,
    get_user_less_than_age,
    get_user_not_active,
    health,
)

urlpatterns = [
    path("health/", health),
    path("user/<uuid:primary_key>", User.as_view()),
    path("users/", Users.as_view(queryset=UserDB.objects.all())),
    path("users/active/true", get_user_active),
    path("users/active/false", get_user_not_active),
    path("users/age/lte/<int:age>", get_user_less_than_age),
    path("users/age/gte/<int:age>", get_user_greater_than_age),
]
