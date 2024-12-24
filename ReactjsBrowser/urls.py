
from django.contrib import admin
from django.urls import path,include
from .views import * 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('snippet',SnippetList.as_view(),name="snippet"),
    path('index',index,name="index")
    
]
