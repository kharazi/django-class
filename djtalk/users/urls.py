from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('list', views.user_list),
    path('login', csrf_exempt(views.login_view))
]