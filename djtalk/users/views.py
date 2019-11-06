import uuid

from django.contrib.auth import authenticate, login 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'GET':
        return render(
            request,
            'login.html',
            context={

            }
        )
    elif request.method == 'POST':

        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            response = redirect(
                '/chat/'
            )
            return response
        else:
            return HttpResponse("Not found", status=404)

def index(request):
    return HttpResponse("<html><title>Salam</title><h1>Salam</h1></html>")


def validate_user_add_request(data):
    if len(data['firstname']) < 2:
        return False, 'Your firstname must be greater than 3 chars', 'firstname'
 
    return True, ''


def user_list(request):
    if request.method == 'POST':
        validate = validate_user_add_request(request.POST)
        if validate[0]:
            u = User(
                first_name=request.POST['firstname'],
                last_name=request.POST['lastname'],
                username=request.POST['username'],
                password='1321',
                avatar='123qwe'
            )
            try:
                u.save()
            except:
                return HttpResponse(
                    "Duplicate",
                    status=400
                )
            return HttpResponse("OK")
        else:
            return HttpResponse("Error", status=400)

    elif request.method == 'GET':
        users = User.objects.all()
        return render(
            request,
            'list.html',
            context={
                'users': users,
                'title': "List User ha",
                'test_dict': {
                    "name": "value"
                }
            }
        )



