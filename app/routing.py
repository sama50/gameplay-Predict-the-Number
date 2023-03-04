from django.urls import path
from app.consumers import ChatConsumer

websocket_urlpatterns =[
    path('ws/wsc/',ChatConsumer.as_asgi())
]