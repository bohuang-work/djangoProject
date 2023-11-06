from django.contrib import admin
from django.urls import path
from userAPI.views import users

urlpatterns = [path("", users)]
