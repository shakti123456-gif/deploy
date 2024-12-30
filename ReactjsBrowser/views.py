from .models import Snippet
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from .rabbitmq import publish_message
from django.http import HttpResponse
from django.shortcuts import render
from .models import *



class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
def index(request):
    # s1=Entry.objects.filter(blog__name__contains="s").select_related("blog").prefetch_related('authors')
    s2 = Entry.objects.filter(mod_date__gt="2023-05-01")
    print(s2)
    return HttpResponse("message pushed to rabbitmq")


