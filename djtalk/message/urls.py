from django.urls import path

from . import views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('message', 
        # csrf_exempt(
            views.MessageView.as_view()
        # )
    ),
    path('message/new', views.add_message),
    path('message/list', views.message_list),
    path('conversation/list', views.conversation_list)
]