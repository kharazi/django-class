from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(
        max_length=100,
        unique=True)
    password = models.CharField(max_length=1000)
    avatar = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    token = models.UUIDField(null=True)


    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


class Messages(models.Model):
    text = models.TextField()
    sender = models.IntegerField()
    receiver = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1) # 1: send 2: receive 3: seen