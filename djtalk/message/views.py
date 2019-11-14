from django.shortcuts import render
from django.contrib.auth.models import User
from message.models import Conversation
from django.http import HttpResponse
from message.models import Messages
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect
from django.http import JsonResponse


def add_message(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            'message': 'Send login request'
        })
    else:
        c = Conversation.objects.get(id=request.POST['conversation'])
        m = Messages(
            text=request.POST['text'],
            sender=request.user,
            conversation=c
        )
        m.save()
        r = {
            'message': 'Your message saved!'
        }
        return JsonResponse(r)


def message_list(request):
    if request.method != 'GET':
        return JsonResponse({
            'message': 'Method not allowed!'
        }, status=405)
    if 'conversation' not in request.GET:
        return JsonResponse({
            'message': 'please send conversation id'
        }, status=400)
    c = Conversation.objects.get(
        id=request.GET['conversation']
    )
    messages = Messages.objects.filter(
        conversation=c
    )
    messages_list = []
    for m in messages:
        messages_list.append(
            {
                'text': m.text,
                'sender': {
                    'first_name': m.sender.first_name,
                    'last_name': m.sender.last_name,
                    'id': m.sender.id
                },
                'date': m.date,
            }
        )

    d = {
        'messages': messages_list
    }
    return JsonResponse(d)



def conversation_list(request):
    conversations = []
    for c in Conversation.objects.all():
        members = []
        for m in c.members.all():

            members.append(
                {
                    'id': m.id,
                    'firstname': m.first_name,
                    'lastname': m.last_name
                }
            )
        conversations.append(
            {
                'id': c.id,
                'name': c.name,
                'is_group': c.is_group,
                'members': members
            }
        )

    return JsonResponse({
        'conversations': conversations
    })
 