from django.db import models
from django.contrib.auth.models import User


class Kiply(models.Model):
    kiply_key = models.CharField(max_length=254, null=True, default=None)
    user = models.OneToOneField(User, related_name='kiply')


class Twitter(models.Model):
    secret = models.CharField(max_length=254, null=True, default=None)
    key = models.CharField(max_length=254, null=True, default=None)
    user = models.OneToOneField(User, related_name='twitter')


