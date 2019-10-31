from django.urls import path

from . import views


urlpatterns = [
    path('<int:conversation_id>', views.chat),
    path('', views.chat),
    path('message/new', views.add_message)

    # path('salam', views.index),
    # path('list', views.user_list),
    # path('add', views.user_add)
]