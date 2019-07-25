from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner
from .filters import SnippetFilter
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = SnippetFilter

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            return serializer.save()
        else:
            return serializer.save(owner=self.request.user)


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
