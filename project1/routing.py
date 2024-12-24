from django.urls import re_path
from . import consumers


# routing.py


websocket_urlpatterns = [
    re_path(r'ws/livec/$', consumers.LiveChatConsumer.as_asgi()),  
]