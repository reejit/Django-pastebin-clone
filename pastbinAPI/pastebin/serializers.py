from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Snippet
from django.contrib.auth.models import User


class SnipprtSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'content', 'created_at', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password', 'snippets']

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
