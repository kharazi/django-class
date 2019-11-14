
from django.contrib.auth import authenticate, login 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.http import JsonResponse


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

    dict_users = []

    for u in users:
        dict_users.append(
            {
                'first_name': u.first_name,
                'last_name': u.last_name,
                'id': u.id
            }
        )
    r = {
        'users': dict_users
    }
    return JsonResponse(r)

  

