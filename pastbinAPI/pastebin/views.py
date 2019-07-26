from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly, IsOwner
from .filters import SnippetFilter


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

    def list(self, request):
        if self.request.user.is_anonymous:
            queryset = Snippet.objects.filter(public=True)
        else:
            queryset = Snippet.objects.filter(
                Q(owner=request.user) | Q(public=True) | Q(share_to=request.user))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Snippet.objects.all()
        snippet = get_object_or_404(queryset, pk=pk)
        if snippet.owner == request.user or snippet.public or request.user in snippet.share_to.all():
            serializer = self.get_serializer(snippet)
            return Response(serializer.data)
        else:
            return Response({'data': 'Not permitted'})


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
