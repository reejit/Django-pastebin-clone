from .models import Snippet
from django.shortcuts import get_object_or_404
from .serializers import SnipprtSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serilaizer = SnipprtSerializer(snippets, many=True)
        return Response(serilaizer.data)

    def post(self, request, format=None):
        serializer = SnipprtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.sav()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    def get(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnipprtSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnipprtSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
