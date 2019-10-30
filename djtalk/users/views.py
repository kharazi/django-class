import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from users.models import Users



def login(request):
    if request.method == 'GET':
        return render(
            request,
            'login.html',
            context={

            }
        )
    elif request.method == 'POST':
        print(request.POST['username'], request.POST['password'])
        u = Users.objects.filter(
            username=request.POST['username'],
            password=request.POST['password']
        )
        print(type(u), u)
        if u:
            u[0].token = uuid.uuid4()
            u[0].save()
            print('sdfsdf', u[0].token)
            response = redirect(
                '/chat/'
            )
            response.set_cookie('token', u[0].token)
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
            u = Users(
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
        users = Users.objects.all()
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


def user_add(request):
   
    print(request.GET)
    p = Person(
        request.GET['firstname'],
        request.GET['lastname'],
        int(request.GET['grade'])
    )
    users.append(p)
    print(p)

    return HttpResponse("Ok! saved!")
