
from django.contrib.auth import authenticate, login 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.http import JsonResponse
from users.serializers import UserSerializer


def login_view(request):

    user = authenticate(
        request=request,
        username=request.POST['username'],
        password=request.POST['password'])
    
    if user:
        login(request, user)
        return JsonResponse({
            'message': 'You are logged in now!'
        })
    else:
        return JsonResponse({
            'message': 'Username or password is wrong!'
        }, status=404)


def user_list(request):
    users = User.objects.all()
    s = UserSerializer(users, many=True)
    r = {
        'users': s.data
    }
    return JsonResponse(r)
