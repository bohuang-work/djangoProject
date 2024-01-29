from django.urls import path

from userAPI.views import UserDetail, UserList, health

urlpatterns = [
    path("health/", health),
    path("users/", UserList.as_view()),
    path("user/<uuid:pk>", UserDetail.as_view()),
]
