from django.shortcuts import render
from users.models import Users
from message.models import Conversation, ConversationMembers
from django.http import HttpResponse
from message.models import Messages
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned



def add_message(request):
    print(request.COOKIES, type(request.COOKIES))
    print('inja', request.POST)
    if 'token' in request.COOKIES:
        token = request.COOKIES['token']
        try:
            u = Users.objects.get(token=token)
            c = Conversation.objects.get(
                id=request.POST['c_id']
            )
            m = Messages(
                text=request.POST['text'],
                sender=u,
                conversation=c
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


def chat(request, conversation_id=None):
    if 'token' in request.COOKIES:
        token = request.COOKIES['token']
        try:
            u = Users.objects.get(token=token)
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
    cm_of_u = ConversationMembers.objects.filter(
        user=u
    )

    if conversation_id:
        c = Conversation.objects.get(
            id=conversation_id
        )
        messages = Messages.objects.filter(
            conversation=c
        )
        return render(
            request,
            'chat.html',
            context={
                'user_conversations': cm_of_u,
                'conversation_id': conversation_id,
                'messages': messages,
            }
        )
    else:
        return render(
            request,
            'chat.html',
            context={
                'user_conversations': cm_of_u,
                'messages': [],
            }
        )