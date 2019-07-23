from rest_framework import serializers
from rest_framework import serializers
from .models import Snippet


class SnipprtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = {'id', 'title', 'content', 'created_at'}
