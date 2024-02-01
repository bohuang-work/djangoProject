from django.urls import path

from userAPI.views import User, Users, health

urlpatterns = [
    path("health/", health),
    path("users/", Users.as_view()),
    path("user/<uuid:pk>", User.as_view()),
]
