from rest_framework import serializers
from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User


class SnipprtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'content', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'snippets']
