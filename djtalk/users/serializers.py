from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.get_full_name()

    class Meta:
        model = User
        exclude = ['password', 'last_login', 'first_name', 'last_name']
