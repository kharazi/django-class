from django.urls import path

from . import views


urlpatterns = [
    path('salam', views.index),
    path('list', views.user_list),
    path('add', views.user_add)
]