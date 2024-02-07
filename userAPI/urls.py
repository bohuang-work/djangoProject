from django.urls import path

from userAPI.views import Job, Jobs, User, Users, health

urlpatterns = [
    path("health/", health),
    path("users/", Users.as_view()),
    path("jobs/", Jobs.as_view()),
    path("user/<uuid:pk>", User.as_view()),
    path("job/<uuid:pk>", Job.as_view()),
]
