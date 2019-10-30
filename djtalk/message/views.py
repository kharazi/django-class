from django.shortcuts import render
from users.models import Users
from django.http import HttpResponse
from users.models import Messages
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def add_message(request):
    print(request.COOKIES, type(request.COOKIES))
    if 'token' in request.COOKIES:
        token = request.COOKIES['token']


        try:
            u = Users.objects.get(token=token)

            m = Messages(
                text=request.POST['text'],
                sender=u.id,
                receiver=request.POST['receiver']
            )
            m.save()
            return HttpResponse("Message Saved!")
        except ObjectDoesNotExist:
            return HttpResponse(
                "Unauthorized! invalid token. Go to login page",
                status=401
            )
        except MultipleObjectsReturned:
            return HttpResponse(
                "Unauthorized! duplicate token. Go to login page",
                status=401
            )
    else:
        return HttpResponse(
            "Unauthorized! Go to login page",
            status=401
        )


def chat(request, user_id=None):
    if user_id:
        second = user_id
        if 'token' in request.COOKIES:
            token = request.COOKIES['token']

            try:
                u = Users.objects.get(token=token)
                self_ = u.id
                messages = Messages.objects.filter(
                    Q(
                        sender=self_, receiver=second
                    ) | Q(
                        sender=second, receiver=self_
                    )
                )
                second_user = Users.objects.get(
                    id=user_id
                )
                
            except ObjectDoesNotExist:
                return HttpResponse(
                    "Unauthorized! invalid token. Go to login page",
                    status=401
                )
            except MultipleObjectsReturned:
                return HttpResponse(
                    "Unauthorized! duplicate token. Go to login page",
                    status=401
                )

                

        return render(
            request,
            'chat.html',
            context={
                'users': Users.objects.all(),
                'receiver': user_id,
                'messages': messages,
                'self_id': u.id,
            }
        )
    else:
        return render(
            request,
            'chat.html',
            context={
                'users': Users.objects.all(),
                'receiver': user_id,
                'messages': [],
                'self_id': '',
            }
        )