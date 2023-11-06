from django.shortcuts import render
from userAPI.models import User
from django.http import JsonResponse


# Create your views here.
def users(request):
    users = User.objects.all()
    return JsonResponse({"users": list(users.values())})
