from django.urls import path

from userAPI.views import (
    Computer,
    Computers,
    Job,
    Jobs,
    Office,
    Offices,
    User,
    Users,
    health,
)

urlpatterns = [
    path("health/", health),
    path("users/", Users.as_view()),
    path("user/<uuid:pk>", User.as_view()),
    path("jobs/", Jobs.as_view()),
    path("job/<uuid:pk>", Job.as_view()),
    path("computers/", Computers.as_view()),
    path("computer/<uuid:pk>", Computer.as_view()),
    path("offices/", Offices.as_view()),
    path("office/<uuid:pk>", Office.as_view()),
]
