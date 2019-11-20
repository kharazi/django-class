
from django.contrib.auth import authenticate, login 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import serializers

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
    

# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     school_name = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.get_full_name()

    class Meta:
        model = User
        exclude = ['password', 'last_login', 'first_name', 'last_name']


def user_list(request):
    users = User.objects.all()

    dict_users = []

    s = UserSerializer(users, many=True)
    print(s.data)

    # for u in users:
    #     s = UserSerializer(u)
    #     dict_users.append(s.data)

    r = {
        'users': s.data
    }
    return JsonResponse(r)


    #     dict_users.append(
    #         {
    #             'first_name': u.first_name,
    #             'last_name': u.last_name,
    #             'id': u.id,
                # ''
    #         }
    #     )
    # r = {
    #     'users': dict_users
    # }
    # return JsonResponse(r)
