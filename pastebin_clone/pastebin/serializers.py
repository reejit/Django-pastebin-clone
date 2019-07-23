from rest_framework import serializers

from .models import UserModel, SnippetModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = {'username', 'password'}


class SnippetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)

    class Meta:
        model = SnippetModel
        fields = '__all__'
